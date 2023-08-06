import pendulum
from pyspark.sql import DataFrame
from pyspark.sql import functions
from pyspark.sql.window import Window

from tecton_core.feature_definition_wrapper import FeatureDefinitionWrapper
from tecton_core.time_utils import convert_timedelta_for_version
from tecton_spark.aggregation_plans import get_aggregation_plan
from tecton_spark.partial_aggregations import TEMPORAL_ANCHOR_COLUMN_NAME


# NOTE: this should _only_ be used by query tree
def construct_full_tafv_df_with_anchor_time(
    fdw: FeatureDefinitionWrapper,
    all_partial_aggregations_df: DataFrame,
) -> DataFrame:
    """Computes full aggregates based on partial aggregates.

    The partial aggregates dataframe must have an "_anchor_time" epoch column that represents the start times of tiles.

    Full aggregates will be computed with respect to all tiles that exist in the partial aggregates dataframe. The
    resulting dataframe will have a "_anchor_time" column, but for each row it will represent the end time (as an epoch)
    of the last tile used in the full aggregate, instead of the start time.

    For a continuous SWAFV, the "_anchor_time" column does not reflect tiles, so regardless of whether there is a spine
    or not, the resulting dataframe will not modify the "_anchor_time" column at all.

    Note that this method currently does not implement any wildcard behavior.

    Args:
        fdw: The feature view to be aggregated. Must be a WAFV.
        all_partial_aggregations_df: The partial aggregates (i.e. tiles) of the feature view. Must contain a timestamp
            column named "_anchor_time" that represents the start times of the tiles.

    Returns:
        A dataframe with the full aggregations. For example, if the feature view has a count aggregation with a window of two days, and the partial aggregates dataframe looks like

        +-------+-----------------+-------------------+
        |user_id|count_transaction|       _anchor_time|
        +-------+-----------------+-------------------+
        |      1|                9|2022-05-13 00:00:00|
        |      1|               22|2022-05-14 00:00:00|
        |      1|               43|2022-05-15 00:00:00|
        +-------+-----------------+-------------------+

        the resulting dataframe would look like

        +-------+-----------------------+-------------------+
        |user_id|transaction_count_3d_1d|       _anchor_time|
        +-------+-----------------------+-------------------+
        |      1|                      9|2022-05-14 00:00:00|
        |      1|                     31|2022-05-15 00:00:00|
        |      1|                     65|2022-05-16 00:00:00|
        +-------+-----------------------+-------------------+

        Note that the "_anchor_time" column has been transformed to reflect end times instead of start times. Also note that for simplicity these examples use timestamps instead of epochs, but in reality the columns must be epochs.
    """
    # TODO: drop anchor time concept from full aggregations. Define start & end times of the aggregation window,
    # use the new concepts for joining, and for returning the temporal aggregate feature dataframes

    # TODO: handle wildcards

    # Since these full aggregations are being performed without a spine, we create a fake timestamp equal to the
    # provided anchor time + tile_interval such that this new fake timestamp completely contains the time range of the
    # full aggregate window. Note that ideally we would either subtract 1 second from the timestamp, due to tiles
    # having [start, end) format, or convert tiles in (start, end] format. For now, we're not doing 1 due to it being
    # confusing in preview, and not doing 2 due to it requiring more work.
    partial_aggregations_df = all_partial_aggregations_df.withColumn(
        TEMPORAL_ANCHOR_COLUMN_NAME,
        functions.col(TEMPORAL_ANCHOR_COLUMN_NAME) + fdw.get_tile_interval_for_version,
    )

    aggregations = []
    time_aggregation = fdw.trailing_time_window_aggregation
    for feature in time_aggregation.features:
        # We do + 1 since RangeBetween is inclusive, and we do not want to include the last row of the
        # previous tile. See https://github.com/tecton-ai/tecton/pull/1110
        window_duration = pendulum.Duration(seconds=feature.window.ToSeconds())
        lower_bound = -(convert_timedelta_for_version(window_duration, fdw.get_feature_store_format_version)) + 1
        window_spec = (
            Window.partitionBy(fdw.join_keys)
            .orderBy(functions.col(TEMPORAL_ANCHOR_COLUMN_NAME).asc())
            .rangeBetween(lower_bound, 0)
        )
        aggregation_plan = get_aggregation_plan(
            feature.function, feature.function_params, time_aggregation.is_continuous, time_aggregation.time_key
        )
        names = aggregation_plan.materialized_column_names(feature.input_feature_name)

        agg = aggregation_plan.full_aggregation_transform(names, window_spec)

        aggregations.append(agg.alias(feature.output_feature_name))

    output_df = partial_aggregations_df.select(fdw.join_keys + [TEMPORAL_ANCHOR_COLUMN_NAME] + aggregations)

    return output_df

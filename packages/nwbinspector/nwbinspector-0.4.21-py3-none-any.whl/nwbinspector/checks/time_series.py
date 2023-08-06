"""Check functions that can apply to any descendant of TimeSeries."""
import numpy as np

from pynwb import TimeSeries

from ..register_checks import register_check, Importance, Severity, InspectorMessage
from ..utils import is_regular_series, is_ascending_series, get_data_shape


@register_check(importance=Importance.BEST_PRACTICE_VIOLATION, neurodata_type=TimeSeries)
def check_regular_timestamps(
    time_series: TimeSeries, time_tolerance_decimals: int = 9, gb_severity_threshold: float = 1.0
):
    """If the TimeSeries uses timestamps, check if they are regular (i.e., they have a constant rate)."""
    if (
        time_series.timestamps is not None
        and len(time_series.timestamps) > 2
        and is_regular_series(series=time_series.timestamps, tolerance_decimals=time_tolerance_decimals)
    ):
        timestamps = np.array(time_series.timestamps)
        if timestamps.size * timestamps.dtype.itemsize > gb_severity_threshold * 1e9:
            severity = Severity.HIGH
        else:
            severity = Severity.LOW
        return InspectorMessage(
            severity=severity,
            message=(
                "TimeSeries appears to have a constant sampling rate. "
                f"Consider specifying starting_time={time_series.timestamps[0]} "
                f"and rate={time_series.timestamps[1] - time_series.timestamps[0]} instead of timestamps."
            ),
        )


@register_check(importance=Importance.CRITICAL, neurodata_type=TimeSeries)
def check_data_orientation(time_series: TimeSeries):
    """If the TimeSeries has data, check if the longest axis (almost always time) is also the zero-axis."""
    if time_series.data is None:
        return

    data_shape = get_data_shape(time_series.data)
    if any(np.array(data_shape[1:]) > data_shape[0]):
        return InspectorMessage(
            message=(
                "Data may be in the wrong orientation. Time should be in the first dimension, and is usually the "
                "longest dimension. Here, another dimension is longer."
            ),
        )


@register_check(importance=Importance.CRITICAL, neurodata_type=TimeSeries)
def check_timestamps_match_first_dimension(time_series: TimeSeries):
    """
    If the TimeSeries has timestamps, check if their length is the same as the zero-axis of data.

    Best Practice: :ref:`best_practice_data_orientation`
    """
    if time_series.data is None or time_series.timestamps is None:
        return

    timestamps_shape = get_data_shape(time_series.timestamps)
    data_shape = get_data_shape(time_series.data)
    if data_shape[0] != timestamps_shape[0]:
        return InspectorMessage(
            message=(
                f"The length of the first dimension of data ({data_shape[0]}) "
                f"does not match the length of timestamps ({timestamps_shape[0]})."
            )
        )


@register_check(importance=Importance.BEST_PRACTICE_VIOLATION, neurodata_type=TimeSeries)
def check_timestamps_ascending(time_series: TimeSeries, nelems=200):
    """Check that the values in the timestamps array are strictly increasing."""
    if time_series.timestamps is not None and not is_ascending_series(time_series.timestamps, nelems=nelems):
        return InspectorMessage(f"{time_series.name} timestamps are not ascending.")


@register_check(importance=Importance.BEST_PRACTICE_VIOLATION, neurodata_type=TimeSeries)
def check_missing_unit(time_series: TimeSeries):
    """
    Check if the TimeSeries.unit field is empty.

    Best Practice: :ref:`best_practice_unit_of_measurement`
    """
    if not time_series.unit:
        return InspectorMessage(
            message="Missing text for attribute 'unit'. Please specify the scientific unit of the 'data'."
        )


@register_check(importance=Importance.BEST_PRACTICE_VIOLATION, neurodata_type=TimeSeries)
def check_resolution(time_series: TimeSeries):
    """Check the resolution value of a TimeSeries for proper format (-1.0 or NaN for unknown)."""
    if time_series.resolution is None or time_series.resolution == -1.0:
        return
    if time_series.resolution <= 0:
        return InspectorMessage(
            message=f"'resolution' should use -1.0 or NaN for unknown instead of {time_series.resolution}."
        )

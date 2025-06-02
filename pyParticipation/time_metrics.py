### Time Metrics Functions

def intervals_between_visits(df: pd.DataFrame, id_col: str, actual_time_col: str) -> pd.Series:
    """
    Computes intervals (in days) between consecutive visits for each participant.

    Args:
        df (pd.DataFrame): DataFrame with longitudinal data.
        id_col (str): Column identifying participants.
        actual_time_col (str): Column with actual datetime of measurements.

    Returns:
        pd.Series: Series of time intervals in days.
    """
    df_sorted = df[[id_col, actual_time_col]].dropna().sort_values([id_col, actual_time_col])
    df_sorted[actual_time_col] = pd.to_datetime(df_sorted[actual_time_col])

    intervals = (
        df_sorted.groupby(id_col)[actual_time_col]
        .diff()
        .dropna()
        .dt.days
    )

    return intervals


def interval_summary_statistics(intervals: pd.Series) -> dict:
    """
    Provides summary statistics for intervals between visits.

    Args:
        intervals (pd.Series): Intervals between visits.

    Returns:
        dict: Summary statistics (median, mean, min, max, quartiles).
    """
    pass


def compute_time_deviations(df: pd.DataFrame, actual_time_col: str, nominal_time_col: str) -> pd.Series:
    """
    Computes deviations between actual and nominal measurement times.

    Args:
        df (pd.DataFrame): DataFrame containing data.
        actual_time_col (str): Column with actual measurement times.
        nominal_time_col (str): Column with planned measurement times.

    Returns:
        pd.Series: Deviations in measurement times.
    """
    pass


def deviation_summary_statistics(deviations: pd.Series) -> dict:
    """
    Provides summary statistics of deviations between actual and nominal times.

    Args:
        deviations (pd.Series): Series containing time deviations.

    Returns:
        dict: Summary statistics (median, mean, min, max, quartiles).
    """
    pass


def measurement_time_distribution(df: pd.DataFrame, time_metric_col: str, time_col: str) -> pd.DataFrame:
    """
    Computes distribution of a selected time metric (e.g., age) at each measurement occasion.

    Args:
        df (pd.DataFrame): DataFrame containing participation data.
        time_metric_col (str): Column of the chosen time metric (e.g., age).
        time_col (str): Column indicating measurement occasions (waves).

    Returns:
        pd.DataFrame: Summary statistics of time metric per measurement occasion.
    """
    pass

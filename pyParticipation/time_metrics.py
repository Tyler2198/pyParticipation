### Time Metrics Functions

def intervals_between_visits(df: pd.DataFrame, id_col: str, actual_time_col: str) -> pd.DataFrame:
    """
    Computes intervals (in days) between consecutive visits for each participant,
    returning a tidy DataFrame with participant ID and interval.

    Args:
        df (pd.DataFrame): DataFrame with longitudinal data.
        id_col (str): Column identifying participants.
        actual_time_col (str): Column with actual datetime of measurements.

    Returns:
        pd.DataFrame: DataFrame with [id_col, interval_days] where each row is a
                      valid interval between consecutive visits (NaNs skipped).
    """
    df_sorted = df[[id_col, actual_time_col]].dropna().copy()
    df_sorted[actual_time_col] = pd.to_datetime(df_sorted[actual_time_col], errors='coerce')
    df_sorted = df_sorted.dropna().sort_values(by=[id_col, actual_time_col])

    # Compute time differences within each patient
    df_sorted['interval_days'] = df_sorted.groupby(id_col)[actual_time_col].diff().dt.days

    # Drop first visit per subject (no previous visit to compute interval from)
    interval_df = df_sorted.dropna(subset=['interval_days'])

    return interval_df[[id_col, 'interval_days']].reset_index(drop=True)



def interval_summary_statistics_by_patient(interval_df: pd.DataFrame, id_col: str = 'USUBJID') -> pd.DataFrame:
    """
    Computes summary statistics (mean, median, min, max, Q1, Q3, count)
    of visit intervals per participant.

    Args:
        interval_df (pd.DataFrame): DataFrame with [id_col, 'interval_days'].
        id_col (str): Column identifying participants.

    Returns:
        pd.DataFrame: DataFrame with interval statistics for each participant.
    """
    grouped = interval_df.groupby(id_col)['interval_days']

    summary = grouped.agg(
        interval_count='count',
        interval_mean='mean',
        interval_median='median',
        interval_min='min',
        interval_q1=lambda x: x.quantile(0.25),
        interval_q3=lambda x: x.quantile(0.75),
        interval_max='max'
    ).reset_index()

    return summary

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

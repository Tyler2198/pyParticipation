### Participation Summary Functions

"""
Participation Summary Module
-----------------------------

This module provides functions to summarize participation patterns in longitudinal studies.
It supports clinical datasets (e.g., CDISC ADaM), with utilities to compute:

- Number of participants
- Number of valid measurements
- Distribution of measurements per participant
- Measurement counts per wave or scheduled occasion
- Inclusion of unscheduled/unknown data

Intended for pre-modeling IDA (Initial Data Analysis) workflows as recommended by STRATOS guidelines.

Author: Denis L. Cascino
Date: 31-05-2025
"""

import pandas as pd

def count_participants(df: pd.DataFrame, id_col: str) -> int:
    """
    Count the number of unique participants in the dataset.

    Args:
        df (pd.DataFrame): Input DataFrame.
        id_col (str): Column name containing unique participant identifiers.

    Returns:
        int: Total number of unique participants.
    """
    return df[id_col].nunique()
  

def count_measurements(df: pd.DataFrame, measurement_col: str) -> int:
    """
    Count the number of valid (non-missing) measurements in the dataset.

    Args:
        df (pd.DataFrame): Input DataFrame.
        measurement_col (str): Column name containing measurement values.

    Returns:
        int: Total number of valid (non-missing) measurements.
    """
    return df[measurement_col].notna().sum()


def participant_measurement_summary(df: pd.DataFrame, id_col: str, measurement_col: str) -> pd.Series:
    """
    Summarize the distribution of valid measurements per participant, including those with 0.

    Args:
        df (pd.DataFrame): Input DataFrame.
        id_col (str): Column name containing participant IDs.
        measurement_col (str): Column containing measurement values.

    Returns:
        pd.Series: Summary statistics (count, mean, std, min, quartiles, max).
    """
    counts_df = measurements_per_participant(df, id_col, measurement_col)
    return counts_df['measurement_count'].describe()


def measurements_per_participant(df: pd.DataFrame, id_col: str, measurement_col: str) -> pd.DataFrame:
    """
    Count valid (non-missing) measurements for each participant, including 0 for those with none.

    Args:
        df (pd.DataFrame): Input DataFrame.
        id_col (str): Column name containing participant IDs.
        measurement_col (str): Column containing measurement values.

    Returns:
        pd.DataFrame: DataFrame with participant IDs and their respective measurement counts.
    """
    all_participants = df[[id_col]].drop_duplicates()

    valid = df[df[measurement_col].notna()]

    counts = valid.groupby(id_col).size().reset_index(name='measurement_count')

    result = all_participants.merge(counts, on=id_col, how='left')
    result['measurement_count'] = result['measurement_count'].fillna(0).astype(int)

    return result


def measurements_per_wave(df: pd.DataFrame, time_col: str, measurement_col: str, include_unscheduled: bool = True) -> pd.Series:
    """
    Count valid (non-missing) measurements per wave/time point, including optional 'UNSCHEDULED'.

    Args:
        df (pd.DataFrame): Input DataFrame.
        time_col (str): Column representing planned time points (e.g., visit number).
        measurement_col (str): Column containing measurement values.
        include_unscheduled (bool, optional): Whether to include a 'UNSCHEDULED/UNKNOWN' category
            for valid measurements lacking a time point. Defaults to True.

    Returns:
        pd.Series: Series indexed by wave (as strings), with counts of valid measurements.
    """
    valid_df = df[df[measurement_col].notna()]

    scheduled = valid_df[valid_df[time_col].notna()]
    counts = scheduled.groupby(time_col).size()

    all_waves = df[time_col].dropna().unique()
    full_counts = pd.Series(data=0, index=sorted(all_waves), dtype=int)
    full_counts.update(counts)

    if include_unscheduled:
        unsched_count = valid_df[valid_df[time_col].isna()].shape[0]
        full_counts = pd.concat([full_counts, pd.Series({'UNSCHEDULED/UNKNOWN': unsched_count})])

    full_counts.index = full_counts.index.map(
    lambda x: str(int(x)) if isinstance(x, (int, float)) and x == int(x) else str(x)
)

    return full_counts

### Participation Summary Functions

def count_participants(df: pd.DataFrame, id_col: str) -> int:
    """
    Counts total unique participants.

    Args:
        df (pd.DataFrame): DataFrame containing participation data.
        id_col (str): Column name for unique participant IDs.

    Returns:
        int: Total number of unique participants.
    """
    return df[id_col].nunique()
  

def count_measurements(df: pd.DataFrame, measurement_col: str) -> int:
    """
    Counts total number of measurements, net of missing values.

    Args:
        df (pd.DataFrame): DataFrame containing participation data.
        measurement_col (str): Measurement column we want to consider to count measurements taken in the longitudinal study.

    Returns:
        int: Total number of measurements.
    """
    return df[measurement_col].notna().sum()


def participant_measurement_summary(df: pd.DataFrame, id_col: str, measurement_col: str) -> pd.Series:
    """
    Provides distribution summary of measurements per participant.

    Args:
        df (pd.DataFrame): DataFrame containing participation data.
        id_col (str): Column name for unique participant IDs.
        measurement_col (str): Measurement column under consideration.

    Returns:
        pd.Series: Summary statistics including mean, median, min, max, and quartiles.
    """
    counts_df = measurements_per_participant(df, id_col, measurement_col)
    return counts_df['measurement_count'].describe()


def measurements_per_participant(df: pd.DataFrame, id_col: str, measurement_col: str) -> pd.DataFrame:
    """
    Provides the count of measurements per participant.

    Args:
        df (pd.DataFrame): DataFrame containing participation data.
        id_col (str): Column name for unique participant IDs.
        measurement_col (str): Measurement column under consideration.

    Returns:
        pd.DataFrame: Participant ID and their respective measurement counts.
    """
    all_participants = df[[id_col]].drop_duplicates()

    valid = df[df[measurement_col].notna()]

    counts = valid.groupby(id_col).size().reset_index(name='measurement_count')

    result = all_participants.merge(counts, on=id_col, how='left')
    result['measurement_count'] = result['measurement_count'].fillna(0).astype(int)

    return result


def measurements_per_wave(df: pd.DataFrame, time_col: str, measurement_col: str) -> pd.Series:
    """
    Counts valid (non-missing) measurements at each wave, including waves with 0 valid measurements.

    Args:
        df (pd.DataFrame): DataFrame with participation data.
        time_col (str): Column indicating measurement occasions (e.g., wave).
        measurement_col (str): Column representing the actual measurement values.

    Returns:
        pd.Series: Series indexed by wave, with count of valid measurements per wave.
    """
    all_waves = df[time_col].dropna().unique()
    
    valid_df = df[df[measurement_col].notna()]
    
    counts = valid_df[time_col].value_counts().sort_index()

    full_counts = pd.Series(index=sorted(all_waves), dtype=int)
    full_counts.update(counts)
    full_counts = full_counts.fillna(0).astype(int)

    return full_counts

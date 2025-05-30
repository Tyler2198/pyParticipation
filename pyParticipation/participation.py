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


def participant_measurement_summary(df: pd.DataFrame, id_col: str) -> pd.Series:
    """
    Provides distribution summary of measurements per participant.

    Args:
        df (pd.DataFrame): DataFrame containing participation data.
        id_col (str): Column name for unique participant IDs.

    Returns:
        pd.Series: Summary statistics including mean, median, min, max, and quartiles.
    """
    pass


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


def measurements_per_wave(df: pd.DataFrame, time_col: str) -> pd.Series:
    """
    Counts measurements at each wave or measurement occasion.

    Args:
        df (pd.DataFrame): DataFrame containing participation data.
        time_col (str): Column name indicating measurement occasions (waves).

    Returns:
        pd.Series: Count of measurements per wave.
    """
    pass

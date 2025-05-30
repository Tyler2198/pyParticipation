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
    pass
  

def count_measurements(df: pd.DataFrame) -> int:
    """
    Counts total number of measurements.

    Args:
        df (pd.DataFrame): DataFrame containing participation data.

    Returns:
        int: Total number of measurements.
    """
    pass


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


def measurements_per_participant(df: pd.DataFrame, id_col: str) -> pd.DataFrame:
    """
    Provides the count of measurements per participant.

    Args:
        df (pd.DataFrame): DataFrame containing participation data.
        id_col (str): Column name for unique participant IDs.

    Returns:
        pd.DataFrame: Participant ID and their respective measurement counts.
    """
    pass


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

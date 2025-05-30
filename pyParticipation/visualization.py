### Visualization functions for participation and timemetrics

def plot_participation_distribution(df: pd.DataFrame, id_col: str, time_col: str, figsize=(10,6)):
    """
    Creates a professional bar plot/histogram showing participant distributions across measurement occasions.

    Args:
        df (pd.DataFrame): DataFrame with participation data.
        id_col (str): Participant ID column.
        time_col (str): Column indicating measurement occasions (waves).
        figsize (tuple): Figure size for the plot.

    Returns:
        matplotlib.figure.Figure: Figure object suitable for further customization or saving.
    """
    pass


def plot_participation_matrix(df: pd.DataFrame, id_col: str, time_col: str, figsize=(12,8)):
    """
    Generates a professional heatmap visualizing participation patterns of each participant across measurement occasions.

    Args:
        df (pd.DataFrame): DataFrame with participation data.
        id_col (str): Participant ID column.
        time_col (str): Column indicating measurement occasions (waves).
        figsize (tuple): Figure size for the heatmap.

    Returns:
        matplotlib.figure.Figure: Figure object suitable for publication.
    """
    pass


def plot_time_metric_distributions(df: pd.DataFrame, time_col: str, metric_col: str, plot_type: str = 'box', figsize=(10,6)):
    """
    Creates professional boxplots or histograms showing the distribution of selected time metrics across measurement occasions.

    Args:
        df (pd.DataFrame): DataFrame containing participation data.
        time_col (str): Column indicating measurement occasions (waves).
        metric_col (str): Column of the chosen time metric (e.g., age).
        plot_type (str): 'box' for boxplot, 'hist' for histogram.
        figsize (tuple): Figure size for the plot.

    Returns:
        matplotlib.figure.Figure: Figure object for saving or further customization.
    """
    pass

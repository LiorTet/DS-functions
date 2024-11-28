import matplotlib.pyplot as plt
import pandas as pd

# Histogram for numerical feature
def plot_count_distribution(
    data_series,
    plot_size=(10, 6),
    tick_interval=1,
    label_rotation=45,
    plot_title="Distribution of Element Counts",
    x_label="Categories",
    y_label="Counts",
):
    """
    Plots a distribution of counts as a bar chart with customizable parameters.

    Parameters:
    - data_series: Pandas Series, the distribution of counts to plot and bins values.
      The index represents categories, and the values are the counts.
    - plot_size: tuple, the size of the plot (default is (10, 6)).
    - tick_interval: int, the interval for x-axis tick marks (default is 1, meaning every tick is shown).
    - label_rotation: int, the rotation angle for x-axis labels (default is 45 degrees).
    - plot_title: str, the title of the plot (default is "Distribution of Element Counts").
    - x_label: str, the label for the x-axis (default is "Categories").
    - y_label: str, the label for the y-axis (default is "Counts").
    """
    # Create the plot
    plt.figure(figsize=plot_size)
    data_series.plot(kind="bar", color="skyblue", edgecolor="black")

    # Set labels and title
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.title(plot_title)

    # Set x-tick interval and rotation
    plt.xticks(
        ticks=range(0, len(data_series), tick_interval),
        labels=data_series.index[::tick_interval],
        rotation=label_rotation,
    )

    # Adjust layout and display the plot
    plt.tight_layout()
    plt.show()


# Create histogram data with custom bins to numerical feature
def calculate_price_histogram(df, price_column="price", bins=10):
    """
    Calculates histogram data for a continuous column with a specified number of bins.

    Parameters:
    - df: DataFrame containing the price data.
    - price_column: str, the name of the column with prices (default is 'price').
    - bins: int, the number of bins for the histogram.

    Returns:
    - histogram_df: DataFrame with bin ranges and counts for each bin.
    """
    # Perform binning and calculate counts in each bin
    binned_data = pd.cut(df[price_column], bins=bins)
    count = binned_data.value_counts(sort=False)

    # Convert to DataFrame for easier access and manipulation
    histogram_df = pd.DataFrame({"bin_range": count.index, "count": count.values})

    return histogram_df


# Create histogram for categorical feature
def calculate_brand_frequency(df, brand_column="brand", top_n=None):
    """
    Calculates the frequency of each brand in the specified column.

    Parameters:
    - df: DataFrame containing the brand data.
    - brand_column: str, the name of the column with brand names (default is 'brand').
    - top_n: int, if provided, limits the result to the top N brands by frequency.

    Returns:
    - brand_frequency_df: DataFrame with brand names and their frequencies.
    """
    # Get the count of each brand
    brand_counts = df[brand_column].value_counts()

    # If top_n is specified, limit to the top N brands
    if top_n:
        brand_counts = brand_counts.head(top_n)

    # Convert to DataFrame for easier handling
    brand_frequency_df = brand_counts.reset_index()
    brand_frequency_df.columns = [brand_column, "count"]

    return brand_frequency_df


# Histogram for categorical feature horizontal
def plot_brand_frequency(
    brand_frequency_df,
    brand_column="brand",
    figsize=(10, 8),
    title="Frequency Distribution of Categories",
):
    """
    Plots a horizontal bar chart for the frequency distribution of brands.

    Parameters:
    - brand_frequency_df: DataFrame, contains 'brand' and 'count' columns from calculate_brand_frequency.
    - brand_column: str, the name of the brand column in the DataFrame (default is 'brand').
    - figsize: tuple, size of the plot (default is (10, 8)).
    - title: str, the title of the plot (default is 'Frequency Distribution of Categories').

    Returns:
    - None: Displays the horizontal bar chart.
    """
    # Sort the DataFrame by count in descending order for a better visual order
    brand_frequency_df = brand_frequency_df.sort_values(by="count", ascending=True)

    # Plotting
    plt.figure(figsize=figsize)
    plt.barh(
        brand_frequency_df[brand_column],
        brand_frequency_df["count"],
        color="skyblue",
        edgecolor="black",
    )

    # Set labels and title
    plt.xlabel("Frequency")
    plt.ylabel("Category")
    plt.title(title)

    # Display the plot
    plt.tight_layout()
    plt.show()

import matplotlib.pyplot as plt
from wordcloud import WordCloud


def plot_brand_wordcloud(df,
                          brand_column='brand',
                          top_n=None,
                          width=800,
                          height=400,
                          plot_size=(10, 6),
                          title='Brand Frequency Word Cloud'):
    """
    Plots a word cloud where the size of each brand is proportional to its frequency.

    Parameters:
    - df: DataFrame containing the brand data.
    - brand_column: str, the name of the column with brand names (default is 'brand').
    - top_n: int, if provided, limits the result to the top N brands by frequency.
    - width: int, the width of the word cloud image (default is 800).
    - height: int, the height of the word cloud image (default is 400).
    - plot_size: tuple, the size of the plot (default is (10, 6)).
    - title: str, the title of the word cloud plot (default is 'Brand Frequency Word Cloud').

    Returns:
    - None: Displays the word cloud plot.
    """
    # Calculate the brand frequencies
    brand_frequency = df[brand_column].value_counts()

    # Limit to top N brands if specified
    if top_n:
        brand_frequency = brand_frequency.head(top_n)

    # Create a dictionary where keys are brands and values are their counts
    brand_freq_dict = brand_frequency.to_dict()

    # Create the word cloud
    wordcloud = WordCloud(width=width, height=height, background_color='white').generate_from_frequencies(brand_freq_dict)

    # Plot the word cloud
    plt.figure(figsize=plot_size)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')  # Hide the axes for better aesthetics
    plt.title(title)
    plt.show()

# X-Y plot to compare two variables
def plot_customer_event_counts(customer_event_counts,
                               column_1='add2cart_count',
                               column_2='wishlist_count',
                               label='Equal Add-to-Cart & Wishlist',
                               title='Customer Event Counts: Add-to-Cart vs. Wishlist',
                               axis_limit=100):
    """
    Plots a scatter plot of add2cart_count vs. wishlist_count for each customer,
    with axes limited to a predetermined range.

    Parameters:
    - customer_event_counts: DataFrame with columns ['customer_id', 'add2cart_count', 'wishlist_count'].
    - column_1: str, the name of the column for add-to-cart counts (default is 'add2cart_count').
    - column_2: str, the name of the column for wishlist counts (default is 'wishlist_count').
    - label: str, label for the diagonal reference line (default is 'Equal Add-to-Cart & Wishlist').
    - title: str, the title of the plot (default is 'Customer Event Counts: Add-to-Cart vs. Wishlist').
    - axis_limit: int, maximum limit for both x and y axes (default is 100).

    Returns:
    - None: Displays the scatter plot.
    """
    plt.figure(figsize=(8, 8))

    # Scatter plot of add2cart_count vs. wishlist_count
    plt.scatter(
        customer_event_counts[column_1],
        customer_event_counts[column_2],
        alpha=0.6,
        edgecolor='black'
    )

    # Diagonal reference line (y=x)
    plt.plot([0, axis_limit], [0, axis_limit], 'r--', label=label)

    # Set plot limits, labels, and title
    plt.xlim(0, axis_limit)
    plt.ylim(0, axis_limit)
    plt.xlabel(column_1)
    plt.ylabel(column_2)
    plt.title(title)
    plt.legend()

    # Show plot with grid
    plt.grid(True)
    plt.show()

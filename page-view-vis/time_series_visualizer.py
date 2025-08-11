import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
# Thanks https://stackoverflow.com/a/17468012 for parse_dates
df = pd.read_csv('fcc-forum-pageviews.csv', parse_dates=['date'])

# Clean data
df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]

def draw_line_plot():
    # Draw line plot
    # Thanks https://matplotlib.org/stable/gallery/lines_bars_and_markers/simple_plot.html for guide on drawing line plots
    fig, ax = plt.subplots() # Create the figure
    ax.plot(df.date, df.value, 'crimson') # Plot the x and y values
    ax.set(xlabel='Date', ylabel='Page Views', title='Daily freeCodeCamp Forum Page Views 5/2016-12/2019') # Axis labels
    fig.set_figwidth(15) # Width of figure, thanks https://matplotlib.org/stable/api/_as_gen/matplotlib.figure.Figure.set_figwidth.html

    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy() # Thanks https://www.geeksforgeeks.org/python/difference-between-shallow-copy-vs-deep-copy-in-pandas-dataframes/ for copy()
    # Thanks https://stackoverflow.com/a/53689762 for dt
    # month column is named "Months" so that gets printed in the legend, this is easier than creating an entire new legend
    df_bar['Months'] = df_bar['date'].dt.month_name()
    df_bar['year'] = df_bar['date'].dt.year

    # Specify custom order for months
    # Thanks https://datascientyst.com/convert-column-to-categorical-pandas-dataframe-examples/ for category
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    df_bar['Months'] = pd.Categorical(df_bar['Months'], categories=months, ordered=True)

    # Convert data to pivot table, get mean for months of each year
    # Thanks https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.pivot_table.html for pivot_table
    pivot = df_bar.pivot_table(index='year', columns='Months', values='value', aggfunc="mean")

    # Draw bar plot
    ax = pivot.plot(kind="bar")
    ax.set(xlabel='Years', ylabel='Average Page Views') # Axis labels
    fig = ax.get_figure()
    fig.set_figwidth(8)
    fig.set_figheight(6.5)

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Specify custom order for months, same method as for bar plot
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    df_box['month'] = pd.Categorical(df_box['month'], categories=months, ordered=True)

    # Draw box plots (using Seaborn)
    # Thanks https://stackoverflow.com/a/16393023 for idea of multiple axes
    fig, ax = plt.subplots(1,2)
    # Thanks https://seaborn.pydata.org/generated/seaborn.boxplot.html for boxplot
    fig = sns.boxplot(data=df_box, x="year", y="value", hue="year", ax=ax[0], legend=False)
    ax[0].set(xlabel="Year", ylabel="Page Views", title="Year-wise Box Plot (Trend)")
    fig = sns.boxplot(data=df_box, x="month", y="value", hue="month", ax=ax[1], legend=False)
    ax[1].set(xlabel="Month", ylabel="Page Views", title="Month-wise Box Plot (Seasonality)")
    fig = ax[0].get_figure()
    fig.set_figwidth(16)
    fig.set_figheight(6.5)

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig

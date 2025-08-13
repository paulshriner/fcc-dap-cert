import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(data=df, x="Year", y="CSIRO Adjusted Sea Level")
    plt.xlim(1850, 2075) # Thanks https://stackoverflow.com/a/25015649 for xlim

    # Create first line of best fit
    # Thanks https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.linregress.html for linregress syntax
    res1 = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    yr_range1 = range(df['Year'].min(), 2051)
    plt.plot(yr_range1, res1.intercept + res1.slope * yr_range1, 'r')

    # Create second line of best fit
    df_y2k = df[df['Year'] >= 2000]
    res2 = linregress(df_y2k['Year'], df_y2k['CSIRO Adjusted Sea Level'])
    yr_range2 = range(2000, 2051)
    plt.plot(yr_range2, res2.intercept + res2.slope * yr_range2, 'r')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
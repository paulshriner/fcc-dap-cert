import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
# Thanks https://numpy.org/doc/stable/reference/generated/numpy.where.html for where
# Need to divide height by 100 to go from cm to m
df['overweight'] = np.where(df.weight / (df.height / 100) ** 2 > 25, 1, 0)

# 3
df['cholesterol'] = np.where(df.cholesterol > 1, 1, 0)
df['gluc'] = np.where(df.gluc > 1, 1, 0)

# 4
def draw_cat_plot():
    # 5
    df_cat = df.melt(id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6
    # Thanks https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html for groupby
    # Thanks https://stackoverflow.com/a/70032669 for size and reset_index
    df_cat = df_cat.groupby(['cardio','variable','value']).size().reset_index(name='total')

    # 7
    # Thanks https://seaborn.pydata.org/generated/seaborn.catplot.html for catplot parameters
    fig = sns.catplot(data=df_cat, x="variable", y="total", col="cardio", hue="value", kind="bar")

    # 8
    fig = fig.fig

    # 9
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    # 11
    # Thanks https://www.geeksforgeeks.org/pandas/ways-to-filter-pandas-dataframe-by-column-values/ for filtering column values
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) & (df['height'] >= df['height'].quantile(0.025)) & (df['height'] <= df['height'].quantile(0.975)) & (df['weight'] >= df['weight'].quantile(0.025)) & (df['weight'] <= df['weight'].quantile(0.975))]

    # 12
    # Thanks https://www.geeksforgeeks.org/python/how-to-create-a-correlation-matrix-using-pandas/ for corr()
    corr = df_heat.corr()

    # 13
    # Thanks https://likegeeks.com/seaborn-heatmap-masks/ for creating upper triangle mask
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    # Thanks https://stackoverflow.com/a/72559674 for plt.subplots
    fig, ax = plt.subplots()

    # 15
    # Thanks https://seaborn.pydata.org/generated/seaborn.heatmap.html for sns.heatmap
    sns.heatmap(corr, vmax = .3, center = 0, annot = True, fmt = '.1f', linewidth = .5, square = True, mask = mask)

    # 16
    fig.savefig('heatmap.png')
    return fig

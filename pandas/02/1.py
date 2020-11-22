"""
group by and aggregate
"""

import pandas as pd 

df = pd.read_csv('drinks.csv')

def meta():
    print(df.head(3))

def group():
    #Which continent drinks more beer on average?
    print('-'*10)
    print(df.groupby('continent').beer_servings.mean().sort_values(ascending=False))

    #For each continent print the statistics for wine consumption.
    print('-'*10)
    print(df.groupby('continent').wine_servings.describe())

    # Print the mean alcohol consumption per continent for every column
    print('-'*10)
    print(df.groupby('continent').mean())

def aggr():
    print('-'*10)
    print(df.groupby('continent').spirit_servings.agg(['mean', 'min', 'max']))

#group()
aggr()
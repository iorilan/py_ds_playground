"""
delete column
value_counts
group by
std
describe
"""

import pandas as pd 

def run():
    df = pd.read_csv('US_Baby_Names_right.csv')
    print(df.head(5))

    #delete column
    print('delete column')
    del df['Unnamed: 0']
    del df['Id']
    print(df.head(5))

    print('count values by gender ')
    print(df['Gender'].value_counts())

    # you don't want to sum the Year column, so you delete it
    del df["Year"]
    # group the data
    names = df.groupby("Name").sum()
    # print the first 5 observations
    print('before sort')
    print(names.head(5))
    print('after sort')
    # sort it from the biggest value to the smallest one
    print(names.sort_values("Count", ascending = 0).head(5))

    print('What is the name with most occurrences?')
    print(names.Count.idxmax)

    print('What is the median name occurrence?')
    print(names[names.Count == names.Count.median()].head(5))

    print('What is the standard deviation of names?')
    print(names.Count.std())

    print('names describe')
    print(names.describe())



run()

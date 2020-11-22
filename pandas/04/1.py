"""
resample
idxmax
"""

import pandas as pd 
import numpy



def run():
    df = pd.read_csv('US_Crime_Rates_1960_2014.csv')

    print(df.info())
    print('-'*10)
    # convert datetime
    df.Year = pd.to_datetime(df.Year, format='%Y')
    print(df.info())

    print('-'*10)

    # Set the Year column as the index
    print('-'*10)
    df = df.set_index('Year', drop = True)
    print(df.head())

    # del column
    print('-'*10)
    del df['Total']
    print(df.head())

    #resample
    print('before sample----')
    print(df.head(5))
    print('after sample----')
    # Uses resample to sum each decade
    df = df.resample('5AS').sum()

    # Uses resample to get the max value only for the "Population" column
    population = df['Population'].resample('5AS').max()

    # Updating the "Population" column
    df['Population'] = population
    print(df.head(5))

    print('most population--')
    print(df['Population'].sort_values(ascending=False).head(1))
    print('most violent--')
    print(df['Violent'].sort_values(ascending=False).head(1))
    
    #What is the most dangerous decade to live in the US?
    print('-'*10)
    print(df.idxmax(0))


run()
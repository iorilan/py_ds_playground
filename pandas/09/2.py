import pandas as pd
import numpy as np


def run():
    wine = pd.read_csv('wine.data')
    print('current data first 5 rows')
    print(wine.head(5))
    print('after delete multiple columns data:')
    wine = wine.drop(wine.columns[[0,3,6,8,11,12,13]], axis = 1)
    print(wine.head(5))

    print('rename columns')
    wine.columns = ['alcohol', 'malic_acid', 'alcalinity_of_ash', 'magnesium', 'flavanoids', 'proanthocyanins', 'hue']
    print(wine.head(5))


    print('set first 3 rows alcohol value to null')
    wine.iloc[0:3, 0] = np.nan
    print(wine.head(5))

    print('set rows 3 and 4 of magnesium')
    wine.iloc[2:4, 3] = np.nan
    print(wine.head(5))


    print('Fill the value of NaN with the number 10 in alcohol and 100 in magnesium')
    wine.alcohol.fillna(10, inplace = True)
    wine.magnesium.fillna(100, inplace = True)
    print(wine.head(5))

    print('num of missing values:')
    print(wine.isnull().sum())

    print('Use random numbers as index and assign nan value')
    random = np.random.randint(10, size = 10)
    wine.alcohol[random] = np.nan
    print(wine.head(20))

    print('count missing values:')
    print(wine.isnull().sum())

    print('Delete the rows that contain missing values')
    wine = wine.dropna(axis = 0, how = "any")
    print(wine.head())
    print(wine.alcohol.head())

    print('non-null in alcohol')
    mask = wine.alcohol.notnull()
    print(wine.alcohol[mask])

    print('reset index')
    wine = wine.reset_index(drop = True)
    print(wine.head())

run()
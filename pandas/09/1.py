"""
    del column and rows
"""
import pandas as pd
import numpy as np

def run():
    iris = pd.read_csv('iris.data')
    # set columns 
    iris.columns = ['sepal_length','sepal_width', 'petal_length', 'petal_width', 'class']

    print('check missing data ')
    print(pd.isnull(iris).sum())

    print('first 20 row data')
    print(iris.head(20))

    print('after set rows 10 to 29 of the column petal_length to nan')
    iris.iloc[10:30,2:3] = np.nan
    print(iris.head(20))

    print('fill nan to 1')
    iris.petal_length.fillna(1, inplace = True)
    print(iris.head(20))

    print('del class column')
    del iris['class']
    print(iris.head(5))

    print('set first row nan')
    iris.iloc[0:1 ,:] = np.nan
    print(iris.head(5))

    print('del rows with nan value')
    iris = iris.dropna(how='any')
    print(iris.head(5))

    print('reset index start from 0')
    iris = iris.reset_index(drop = True)
    print(iris.head(5))

run()
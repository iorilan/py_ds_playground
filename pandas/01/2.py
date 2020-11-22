"""
meta: describe, shape, column, index, dtypes
column.unique
value_counts
"""

import pandas as pd 
import numpy as np

df = pd.read_csv('u.user', sep='|', index_col='user_id')

def meta():
    # print(df.describe()) # by default only numeric cols
    # print('-'*10)
    # print(df.describe(include='all'))
    # print('-'*10)

    # print(df.head(5))

    # print('-'*10)
    # print(df.tail(3))

    # print('-'*10)
    # # num of rows
    # print(df.shape[0])
    # # num of columns
    # print(df.shape[1])

    # print('-'*10)
    # print(df.columns)
    # print(df.index)
    # print(df.dtypes)
    
    print('-'*10)
    # occupation column data
    print(df.occupation)
    print(df['occupation'])
    print(df.occupation.describe())

def count():
    # unique values 
    print(df.occupation.unique())

    # most freq ,top 3
    print('-'*10)
    print(df.occupation.value_counts().head(3).index[0])
    print(df.occupation.value_counts().head(3).index[1])
    print(df.occupation.value_counts().head(3).index[2])
    # mean age
    print('-'*10)
    print(df.age.mean())
    #age with least occurence
    print('-'*10)
    print(df.age.value_counts().tail(20))


#meta()
count()
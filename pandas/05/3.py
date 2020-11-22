"""
series
reindex
rename column
"""

import pandas as pd
import numpy as np


s1 = pd.Series(np.random.randint(1, high=5, size=100, dtype='l'))
s2 = pd.Series(np.random.randint(1, high=4, size=100, dtype='l'))
s3 = pd.Series(np.random.randint(10000, high=30001, size=100, dtype='l'))

def run ():
    print('cat series axis=1')
    #create data frame from series
    df = pd.concat([s1, s2, s3], axis=1)
    print(df.head(5))

    print('rename column in place')
    df.rename(columns = {0: 'bedrs', 1: 'bathrs', 2: 'price_sqr_meter'}, inplace=True)
    print(df.head(5))

    print('cat series axis=0')
    df2 = pd.concat([s1,s2,s3], axis=0)
    # it is still a Series, so we need to transform it to a DataFrame
    df2 = df2.to_frame()
    print(len(df2))
    print(df2.head(5))
    #only until 99
    print(df2.tail(5))


    print('reindex')
    df2.reset_index(drop=True, inplace=True)
    print(df2.head(5))
    #until 299
    print(df2.tail(5))



run()
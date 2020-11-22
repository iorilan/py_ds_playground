"""
merge data frame 
numpy rand
"""
import pandas as pd
import numpy as np

def run ():
    df1 = pd.read_csv("cars1.csv")
    df2 = pd.read_csv("cars2.csv")

    print('car1-'*5)
    df1=df1.loc[:, 'mpg':'car']
    print(df1.head(5))

    print('car2-'*5)
    print(df2.head(5))

    # merge 
    print('merge-'*5)
    df3 = df1.append(df2)
    print(df3.head(5))

    #add new column
    owner = np.random.randint(15000, high=73001, size=398, dtype='l')
    df3['new_column']=owner
    print(df3.head(5))

run()
"""
    apply and applymap
"""

import pandas as pd 
import numpy




def run():
    df = pd.read_csv('student-mat.csv')
    
    print('-'*10)
    # all rows ,from 'school' until the 'guardian' column 
    print(df.loc[: , "school":"guardian"].head(5))
    print(df.loc[: , "school":"guardian"].tail(5))

    print('-'*10)
    #apply filter : capitalize
    cp=df['Mjob'].apply(lambda x:x.capitalize())
    print(cp.head(5))

    #apply filter: age
    def f(x):
        return x>17
    cp2 = df['age'].apply(f)
    print('-'*10)
    print(cp2.head(5))

    #applymap
    print('-'*10)
    def f2(x):
        if x=='GP':
            return 'GP1'
        return x
    res=df.loc[: , "school":"school"].applymap(f2)
    print(res.head(5))



run()
import pandas as pd
import numpy as np
def create_from_array():
    arr= [1,2,3,4,5,'a','b','c']
    df = pd.DataFrame(arr)
    print(df)
    print('-'*10)
    print(df.head(3))


def create_from_dict():
    data = {
        "student":["jim","tom","neo","hele"],
        "mark":[192,304,203,394],
        "class":[1,2,3,1]
        }
    df = pd.DataFrame(data)
    print(df)
    print('Select Column'+'-'*10)
    print(df[['student','mark']])

    print('iterrows' +'-'*10)
    for i,j in df.iterrows():
        print(i,j)
    
    print('iteritems'+'-'*10)
    for i,j in df.iteritems():
        print(i,j)
    
    print('itertuples'+'-'*10)
    for i in df.itertuples():
        print(*i)
    
    print('itercolumns'+'-'*10)
    cols = list(df)
    for i in cols:
        print(','.join(map(str,df[i])))

def df_add_col():
    data = {
        "student":["jim","tom","neo","hele"],
        "mark":[192,304,203,394],
        "class":[1,2,3,1]
        }
    df = pd.DataFrame(data)
    df['year'] = [1999,2001,1992,1997]
    print(df)

def df_del_col():
    data = {
        "student":["jim","tom","neo","hele"],
        "mark":[192,304,203,394],
        "class":[1,2,3,1]
        }
    df = pd.DataFrame(data)
    df.drop(['class'], axis=1, inplace=True)
    print(df)

    
def drop_na():
    dc = {'First Score':[100, 90, np.nan, 95],
            'Second Score': [30, np.nan, 45, 56],
            'Third Score':[52, 40, 80, 98],
            'Fourth Score':[np.nan, np.nan, np.nan, 65]}
    
    df = pd.DataFrame(dc)
    
    d=df.dropna()
    print(d)

def index():
    dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"], 
        'degree': ["MBA", "BCA", "M.Tech", "MBA"], 
        'score':[90, 40, 80, 98]}     
    df = pd.DataFrame(dict, index = [0,1,2,3]) 
    print(df) 
    print('-'*10)
    print(df[df.index > 2])

def series():
    data = {
        "student":["jim","tom","neo","hele"],
        "mark":[192,304,203,394],
        "class":[1,2,3,1]
        }
    df=pd.DataFrame(data)
    se = pd.Series(df['mark'])
    print(se.head(3))
    

    
    

#create_from_array()
#create_from_dict()
index()
#df_add_col()
#df_del_col()
#drop_na()
#series()
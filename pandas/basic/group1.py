import pandas as pd 
import numpy as np 

def group_by_col():

    data1 = {'Name':['Joe', 'Mark', 'Leo', 'Frank',  
                    'Issac', 'Leo', 'Frank', 'Mark'],  
            'Age':[27, 24, 22, 32,  
                33, 36, 27, 32],  
            'Address':['Street1', 'Street2', 'Street1', 'Street2', 
                    'Street3', 'Street3', 'Street2', 'Street1'],  
            'Education':['Degree', 'MA', 'MA', 'Phd', 
                            'MA', 'Degree', 'Phd', 'MA']}  
    df= pd.DataFrame(data1)
    print(df.groupby('Name').groups)
    print(df.groupby('Address').groups)
    edu = df.groupby('Education')
    for g, e in edu:
        print(g)
        print(e)

def group_by_multi_col():
    data1 = {'Name':['Joe', 'Mark', 'Leo', 'Frank',  
                    'Issac', 'Leo', 'Frank', 'Mark'],  
            'Age':[27, 24, 22, 32,  
                33, 36, 27, 32],  
            'Address':['Street1', 'Street2', 'Street1', 'Street2', 
                    'Street3', 'Street3', 'Street2', 'Street1'],  
            'Education':['Degree', 'MA', 'MA', 'Phd', 
                            'MA', 'Degree', 'Phd', 'MA']}  
    df= pd.DataFrame(data1)
    print(df.groupby(['Name','Address']).groups)

def group_then_sum():
    data1 = {
            'Name':['Frank','Leo','Issac','Dav','Frank','Issac'],
            'Mark':[39,41,95,21,14,99],
            'Age':[12,14,15,11,12,14],
            'Class':[1,1,2,2,1,2]
            }
    df = pd.DataFrame(data1)
    df1 = df.drop(['Age','Class'], axis=1, inplace=False)

    print('-'*10)
    print(df1.groupby(['Name'], sort=True).sum())

    print('-'*10)
    print(df1.groupby(['Name'], sort=True).mean())
    
    print('-'*10)
    grp = df.groupby("Name")
    for n,g in grp:
        print(n)
        print(g)

def get_group():
    data1 = {'Name':['Joe', 'Mark', 'Leo', 'Frank',  
                    'Issac', 'Leo', 'Frank', 'Mark'],  
            'Age':[27, 24, 22, 32,  
                33, 36, 27, 32],  
            'Address':['Street1', 'Street2', 'Street1', 'Street2', 
                    'Street3', 'Street3', 'Street2', 'Street1'],  
            'Education':['Degree', 'MA', 'MA', 'Phd', 
                            'MA', 'Degree', 'Phd', 'MA']}  
    df = pd.DataFrame(data1)
    
    grp = df.groupby(['Name'])
    print(grp.get_group('Frank'))
    grp2 = df.groupby(['Name','Age'])
    print(grp2.get_group(('Frank',27)))

def aggre():
    data1 = {
            'Name':['Frank','Leo','Issac','Dav','Frank','Issac'],
            'Mark':[39,41,95,21,14,99],
            'Age':[12,14,15,11,12,14],
            'Class':[1,1,2,2,1,2]
            }
    df = pd.DataFrame(data1)
    grp = df.groupby('Name')
    print(grp.aggregate(np.sum))
    print(grp['Mark'].agg([np.sum, np.mean, np.std]))
    print(grp.agg({'Mark':'mean','Age':'sum'}))

def trans():
    data1 = {
            'Name':['Frank','Leo','Issac','Dav','Frank','Issac'],
            'Mark':[39,41,95,21,14,99],
            'Age':[12,14,15,11,12,14],
            'Class':[1,1,2,2,1,2]
            }
    df = pd.DataFrame(data1)
    df1 = df.drop(['Class','Age'], axis=1, inplace=False)
    grp = df1.groupby('Name')
    print(grp.transform(lambda x:x-60))

def filter():
    data1 = {
            'Name':['Frank','Leo','Issac','Dav','Frank','Issac'],
            'Mark':[39,41,95,21,14,99],
            'Age':[12,14,15,11,12,14],
            'Class':[1,1,2,2,1,2]
            }
    df = pd.DataFrame(data1)
    grp = df.groupby('Name')
    print(grp.filter(lambda x: len(x)==1))


    
#group_by_col()
#group_by_multi_col()
#group_then_sum()
#get_group()
#aggre()
#trans()
filter()
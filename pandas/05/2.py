"""
concat 
merge
"""

import pandas as pd 

d1 = {
        'subject_id': ['1', '2', '3', '4', '5'],
        'first_name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'], 
        'last_name': ['Anderson', 'Ackerman', 'Ali', 'Aoni', 'Atiches']}

d2 = {
        'subject_id': ['4', '5', '6', '7', '8'],
        'first_name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'], 
        'last_name': ['Bonder', 'Black', 'Balwner', 'Brice', 'Btisan']}

d3 = {
        'subject_id': ['1', '2', '3', '4', '5', '7', '8', '9', '10', '11'],
        'test_id': [51, 15, 15, 61, 16, 14, 15, 1, 61, 16]}

def run():
    df1 = pd.DataFrame(d1)
    df2 = pd.DataFrame(d2)
    df3 = pd.DataFrame(d3)
    print('-'*10)
    print(df1.head(1))
    print(df2.head(1))
    print(df3.head(1))

    #cat 
    print('-'*10)
    df4 = pd.concat([df1,df2])
    print(df4)

    # cat on axis=1
    print('-'*10)
    df5 = pd.concat([df1,df2], axis=1)
    print(df5)

    #merge based on column
    print('merge based on subject id')
    print(pd.merge(df4, df3, on='subject_id', how='inner'))

    print('merge all')
    print(pd.merge(df4, df3, how='outer'))


    #inner join 
    print('-'*10)
    print(pd.merge(df1, df2, on='subject_id', how='inner'))

    #outer join
    print('-'*10)
    print(pd.merge(df1, df2, on='subject_id', how='outer'))


run()

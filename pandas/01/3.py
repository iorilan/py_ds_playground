"""
meta : df.column_name, shape, info
sort_values
str filter : column.str.startswith, column.isin
iloc, loc
"""
import pandas as pd 

df = pd.read_csv('Euro_2012_stats_TEAM.csv', sep=',')

def meta ():
    print(df.Goals)

    print('-'*10)
    # row, col
    print(df.shape[0], df.shape[1])

    print('-'*10)
    print(df.info())

def sort():
    record = df[['Team', 'Yellow Cards', 'Red Cards']]
    print(record.sort_values(['Red Cards','Yellow Cards'], ascending=False))

    print('-'*10)
    print(record['Yellow Cards'].mean(), record['Red Cards'].sum())

def sel():
    print(df.Goals > 5)

    print('-'*10)
    print(df.Team.str.startswith('G'))

    # select first 7 cols
    print('-'*10)
    print(df.iloc[:, 0:7])

    # all cols except last 5
    print('-'*10)
    print(df.iloc[:, :-5])

def filter():
    # select specified team shooting accuracy
    print(df.loc[df.Team.isin(['England', 'Italy', 'Russia']),
    ['Team','Shooting Accuracy']])

#meta()
#sort()
#sel()
filter()
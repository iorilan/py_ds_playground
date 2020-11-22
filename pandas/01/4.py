"""
loc ,iloc
filter: df[df[column] condition value]
"""


import pandas as pd 

raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'],
            'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'],
            'deaths': [523, 52, 25, 616, 43, 234, 523, 62, 62, 73, 37, 35],
            'battles': [5, 42, 2, 2, 4, 7, 8, 3, 4, 7, 8, 9],
            'size': [1045, 957, 1099, 1400, 1592, 1006, 987, 849, 973, 1005, 1099, 1523],
            'veterans': [1, 5, 62, 26, 73, 37, 949, 48, 48, 435, 63, 345],
            'readiness': [1, 2, 3, 3, 2, 1, 2, 3, 2, 1, 2, 3],
            'armored': [1, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1],
            'deserters': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
            'origin': ['Arizona', 'California', 'Texas', 'Florida', 'Maine', 'Iowa', 'Alaska', 'Washington', 'Oregon', 'Wyoming', 'Louisana', 'Georgia']}

df = pd.DataFrame(data=raw_data)
df.set_index('origin', inplace=True)

def cols():
    print('-'*10)
    print(df.veterans)
    print('-'*10)
    print(df[["veterans", "deaths"]])

    print('-'*10)
    print(df.columns)

def sel():
    #Select the 'deaths', 'size' and 'deserters' columns from Maine and Alaska
    print(df.loc[["Maine", "Alaska"], ["deaths", "size", "deserters"]])

    print('-'*10)
    # Select the rows 3 to 7 and the columns 3 to 6
    print(df.iloc[2:7, 2:6])

    print('-'*10)
    #Select every row up to fourth row and exclude last 3 columns
    print(df.iloc[:4, :-3])

    # Select rows where df.deaths is greater than 50
    print('-'*10)
    print(df[df["deaths"] > 50])

    # Select all the regiments not named "Dragoons"
    print('-'*10)
    print(df[df["regiment"] != "Dragoons"])

    print('-'*10)
    #Select the rows called Texas and Arizona
    print(df.loc[["Texas", "Arizona"], :])

    print('-'*10)
    #Select the third cell in the row named Arizona
    print(df.loc[["Arizona"]].iloc[:, 2])
    
    print('-'*10)
    #Select the third value in deaths col
    print(df.loc[:, ["deaths"]].iloc[2])

#cols() 
sel()
"""
group by
"""

import pandas as pd 


raw_data = {'regiment': ['Nighthawks', 'Nighthawks', 'Nighthawks', 'Nighthawks', 'Dragoons', 'Dragoons', 'Dragoons', 'Dragoons', 'Scouts', 'Scouts', 'Scouts', 'Scouts'], 
        'company': ['1st', '1st', '2nd', '2nd', '1st', '1st', '2nd', '2nd','1st', '1st', '2nd', '2nd'], 
        'name': ['Miller', 'Jacobson', 'Ali', 'Milner', 'Cooze', 'Jacon', 'Ryaner', 'Sone', 'Sloan', 'Piger', 'Riani', 'Ali'], 
        'preTestScore': [4, 24, 31, 2, 3, 4, 24, 31, 2, 3, 2, 3],
        'postTestScore': [25, 94, 57, 62, 70, 25, 94, 57, 62, 70, 62, 70]}

df = pd.DataFrame(raw_data, columns = raw_data.keys())

def group():
    # What is the mean preTestScore from the regiment Nighthawks
    print(df[df['regiment'] == 'Nighthawks'].groupby('regiment').mean())

    print('-'*10)
    #Present general statistics by company
    print(df.groupby('company').describe())

    print('-'*10)
    #What is the mean of each company's preTestScore?
    print(df.groupby('company').preTestScore.mean())

    print('-'*10)
    # Present the mean preTestScores grouped by regiment and company
    print(df.groupby(['regiment', 'company']).preTestScore.mean())

    print('-'*10)
    # Present the mean preTestScores grouped by regiment and company without heirarchical indexing
    print(df.groupby(['regiment', 'company']).preTestScore.mean().unstack())

    print('-'*10)
    # Group the entire dataframe by regiment and company
    df.groupby(['regiment', 'company']).mean()

    print('-'*10)
    #What is the number of observations in each regiment and company
    df.groupby(['company', 'regiment']).size()

    #Iterate over a group and print the name and the whole data from the regiment
    print('-'*10)
    for name, group in df.groupby('regiment'):
        print(name)
        print(group)
group()
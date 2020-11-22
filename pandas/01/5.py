"""
group by 
agg
sort_values
apply
"""

import pandas as pd 

df = pd.read_csv('u.user', sep='|', index_col='user_id')

def group():
    #Discover what is the mean age per occupation
    print(df.groupby('occupation').age.mean())

    print('-'*10)
    #Discover the Male ratio per occupation and sort it from the most to the least
    df['gender_n'] = df['gender'].apply(lambda x: 1 if x == 'M' else 0)
    a = df.groupby('occupation').gender_n.sum() / df.occupation.value_counts() * 100 
    print(a.sort_values(ascending = False))

def aggr():
    #For each occupation, calculate the minimum and maximum ages
    print('-'*10)
    print(df.groupby('occupation').age.agg(['min', 'max']))

    print('-'*10)
    #For each combination of occupation and gender, calculate the mean age
    print(df.groupby(['occupation', 'gender']).age.mean())

#For each occupation present the percentage of women and men
def aggr1():
    # create a data frame and apply count to gender
    gender_ocup = df.groupby(['occupation', 'gender']).agg({'gender': 'count'})

    # create a DataFrame and apply count for each occupation
    occup_count = df.groupby(['occupation']).agg('count')

    # divide the gender_ocup per the occup_count and multiply per 100
    occup_gender = gender_ocup.div(occup_count, level = "occupation") * 100

    # present all rows from the 'gender column'
    print(occup_gender.loc[: , 'gender'])


#group()
#aggr()
aggr1()
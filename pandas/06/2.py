import pandas as pd
import datetime

df = pd.read_csv('wind.data.txt', sep = "\s+", parse_dates = [[0,1,2]]) 
# transform Yr_Mo_Dy it to date type datetime64
df["Yr_Mo_Dy"] = pd.to_datetime(df["Yr_Mo_Dy"])
# set 'Yr_Mo_Dy' as the index
df = df.set_index('Yr_Mo_Dy')

def run():
    print('before apply')
    print(df.head(5))
    #fix year 2061
    def fix_century(x):
        year = x.year - 100 if x.year > 1989 else x.year
        return datetime.date(year, x.month, x.day)
    # apply the function fix_century on the column and replace the values to the right ones
    df['Yr_Mo_Dy'] = df['Yr_Mo_Dy'].apply(fix_century)
    print('after apply')
    print(df.head(5))

    # Compute how many values are missing for each location over the entire record.
    print('num of null')
    print(df.isnull().sum())

    print('num of non-null')
    print(df.notnull().sum()) #df.shape[0] - data.isnull().sum()

    print('mean windspeeds of the windspeeds over all the locations and all the times.')
    print(df.sum().sum() / df.notna().sum().sum())

    print('min, max and mean windspeeds and standard deviations')
    print(df.describe(percentiles=[]))

    # Create a DataFrame called day_stats and calculate the min, max and mean windspeed and standard deviations of the windspeeds across all the locations at each day
    # day_stats = pd.DataFrame()

    # # this time we determine axis equals to one so it gets each row.
    # day_stats['min'] = data.min(axis = 1) # min
    # day_stats['max'] = data.max(axis = 1) # max 
    # day_stats['mean'] = data.mean(axis = 1) # mean
    # day_stats['std'] = data.std(axis = 1) # standard deviations

    # day_stats.head()

def run2():
    print('average windspeed in January for each location.')
    print(df.loc[df.index.month == 1].mean())

    print('Downsample the record to a yearly frequency for each location.')
    print(df.groupby(df.index.to_period('A')).mean())

    print('Downsample the record to a monthly frequency for each location.')
    print(df.groupby(df.index.to_period('M')).mean())

    print('Downsample the record to a weekly frequency for each location.')
    print(df.groupby(df.index.to_period('W')).mean())

    print('min, max and mean windspeeds and standard deviations of first 52 weeks.')
    # resample data to 'W' week and use the functions
    weekly = df.resample('W').agg(['min','max','mean','std'])

    # slice it for the first 52 weeks and locations
    print(weekly.loc[weekly.index[1:53], "RPT":"MAL"] .head(10))

#run()
run2()


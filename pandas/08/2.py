import pandas as pd

df1 = pd.read_csv('weekly.csv')

def run():
    #set index column
    df = df1.set_index('Date')

    #set index col type
    df.index = pd.to_datetime(df.index)

    print('Change the frequency to monthly, sum the values and assign it to monthly')
    monthly=df.resample('M').sum()
    print(monthly)

    print('drop NA and resample ')
    monthly2 = monthly[monthly['Total Equity']>0]
    print(monthly2)

    print('resample yearly:')
    yearly = monthly2.resample('AS-JAN').sum()

    print(yearly)

run()
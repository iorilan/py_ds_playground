
"""
resample
"""

import pandas as pd
import numpy as np

# visualization
import matplotlib.pyplot as plt

df = pd.read_csv('appl_1980_2014.csv')
def run():    
    #Transform the Date column as a datetime type
    df.Date = pd.to_datetime(df.Date)
    #set index column
    apple=df.set_index('Date')
    print(apple.head(3))

    print('Is there any duplicate dates?')
    print(apple.index.is_unique)

    #Make the first entry the oldest date.
    apple.sort_index(ascending = True).head()

    print('Get the last business day of each month')
    apple_month = apple.resample('BM').mean()
    print(apple_month.head())

    print('What is the difference in days between the first day and the oldest')
    print((apple.index.max() - apple.index.min()).days)

    print('data by month')    
    apple_months = apple.resample('BM').mean()
    print(apple_months.index)

    print('Plot the [Adj Close] value')
    appl_open = apple['Adj Close'].plot(title = "Apple Stock")

    # changes the size of the graph
    fig = appl_open.get_figure()
    fig.set_size_inches(13.5, 9)
    plt.show()

run()
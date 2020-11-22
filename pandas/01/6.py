#plot data frame

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
chipo = pd.read_csv('chipotle.tsv', sep = '\t')
def plot():
    #Create a histogram of the top 5 items bought
    x = chipo.item_name
    letter_counts = Counter(x)
    df = pd.DataFrame.from_dict(letter_counts, orient='index')
    df = df[0].sort_values(ascending = True)[45:50]
    df.plot(kind='bar')
    plt.xlabel('Items')
    plt.ylabel('Number of Times Ordered')
    plt.title('Most ordered Chipotle\'s Items')
    plt.show()

def plot2():
    #Create a scatterplot with the number of items orderered per order price
    chipo.item_price = [float(value[1:-1]) for value in chipo.item_price] # strip the dollar sign and trailing space
    orders = chipo.groupby('order_id').sum()

    # creates the scatterplot
    # plt.scatter(orders.quantity, orders.item_price, s = 50, c = 'green')
    plt.scatter(x = orders.item_price, y = orders.quantity, s = 50, c = 'green')
    plt.xlabel('Order Price')
    plt.ylabel('Items ordered')
    plt.title('Number of items ordered per order price')
    plt.ylim(0)
    plt.show()

plot2()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="ticks")
online_rt = pd.read_csv('Online_Retail.csv', encoding = 'latin1')

# Create a histogram with the 10 countries that have the most 'Quantity' ordered except UK
def plot():
    # group by the Country
    countries = online_rt.groupby('Country').sum()

    # sort the value and get the first 10 after UK
    countries = countries.sort_values(by = 'Quantity',ascending = False)[1:11]

    # create the plot
    countries['Quantity'].plot(kind='bar')

    # Set the title and labels
    plt.xlabel('Countries')
    plt.ylabel('Quantity')
    plt.title('10 Countries with most orders')

    # show the plot
    plt.show()

def plot2():
    #Create a scatterplot with the Quantity per UnitPrice by CustomerID for the top 3 Countries (except UK)
    online_rt2 = online_rt[online_rt.Quantity > 0]
    # groupby CustomerID
    customers = online_rt2.groupby(['CustomerID','Country']).sum()

    # there is an outlier with negative price
    customers = customers[customers.UnitPrice > 0]

    # get the value of the index and put in the column Country
    customers['Country'] = customers.index.get_level_values(1)

    # top three countries
    top_countries =  ['Netherlands', 'EIRE', 'Germany']

    # filter the dataframe to just select ones in the top_countries
    customers = customers[customers['Country'].isin(top_countries)]

    #################
    # Graph Section #
    #################

    # creates the FaceGrid
    g = sns.FacetGrid(customers, col="Country")

    # map over a make a scatterplot
    g.map(plt.scatter, "Quantity", "UnitPrice", alpha=1)

    # adds legend
    g.add_legend()
    plt.show()

def get_data():
    online_rt2 = online_rt[online_rt.Quantity > 0]
    #Pull data from online_rtfor CustomerIDs 12346.0 and 12347.0.
    #print(online_rt2[online_rt2.CustomerID == 12347.0].sort_values(by='UnitPrice', ascending = False).head())
    #print(online_rt2[online_rt2.CustomerID == 12346.0].sort_values(by='UnitPrice', ascending = False).head())
    sales_volume = online_rt2.groupby('Country').Quantity.sum().sort_values(ascending=False)
    # Find out the top 3 countries in terms of sales volume.
    top3 = sales_volume.index[1:4] #We are excluding UK
    #print(top3)
    #Add a column to online_rt called Revenue calculate the revenue (Quantity * UnitPrice) from each sale
    online_rt2['Revenue'] = online_rt2.Quantity * online_rt2.UnitPrice
    #print(online_rt2.head(5))
    #Group by CustomerID and Country and find out the average price (AvgPrice) each customer spends per unit.
    return online_rt2, top3

def plot3():
    # Group by CustomerID and Country and find out the average price (AvgPrice) each customer spends per unit.
    online_rt2, top3=get_data()
    grouped = online_rt2[online_rt2.Country.isin(top3)].groupby(['CustomerID','Country'])
    plottable = grouped['Quantity','Revenue'].agg('sum')
    plottable['AvgPrice'] = plottable.Revenue / plottable.Quantity
    plottable['Country'] = plottable.index.get_level_values(1)

    g = sns.FacetGrid(plottable, col="Country")
    # map over a make a scatterplot
    g.map(plt.scatter, "Quantity", "AvgPrice", alpha=1)
    # adds legend
    g.add_legend()
    plt.plot()
    plt.show()

def plot4():
    online_rt2,top3 = get_data()
    grouped = online_rt2.groupby(['CustomerID'])
    plottable = grouped['Quantity','Revenue'].agg('sum')
    plottable['AvgPrice'] = plottable.Revenue / plottable.Quantity

    # map over a make a scatterplot
    plt.scatter(plottable.Quantity, plottable.AvgPrice)
    plt.plot()
    plt.show()

def plot5():
    online_rt2, top3=get_data()
    grouped = online_rt2.groupby(['CustomerID','Country'])
    plottable = grouped.agg({'Quantity': 'sum','Revenue': 'sum'})
    plottable['AvgPrice'] = plottable.Revenue / plottable.Quantity

    # map over a make a scatterplot
    plt.scatter(plottable.Quantity, plottable.AvgPrice)

    #Zooming in. (I'm starting the axes from a negative value so that
    #the dots can be plotted in the graph completely.)
    plt.xlim(-40,2000) 
    plt.ylim(-1,80)

    plt.plot()
    plt.show()

#Plot a line chart showing revenue (y) per UnitPrice (x)
def plot6():
    online_rt2, top3 = get_data()
    price_start = 0 
    price_end = 50
    price_interval = 1

    #Creating the buckets to collect the data accordingly
    buckets = np.arange(price_start,price_end,price_interval)

    #Select the data and sum
    revenue_per_price = online_rt2.groupby(pd.cut(online_rt2.UnitPrice, buckets)).Revenue.sum()
    revenue_per_price.plot()

    #Place labels
    plt.xlabel('Unit Price (in buckets of '+str(price_interval)+')') 
    plt.ylabel('Revenue')

    #Even though the data is bucketed in intervals of 1,
    #I'll plot ticks a little bit further apart from each other to avoid cluttering.
    plt.xticks(np.arange(price_start,price_end,3),
            np.arange(price_start,price_end,3))
    plt.yticks([0, 500000, 1000000, 1500000, 2000000, 2500000],
            ['0', '$0.5M', '$1M', '$1.5M', '$2M', '$2.5M'])
    plt.show()
#plot()
#plot2()
#plot3()
#plot4()
#plot5()
plot6()
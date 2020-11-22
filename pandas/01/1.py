"""
meta data : shape, info ,columns, index, drop_duplicates
sort_values 
total: sum , count, value_counts, unique
filter : df[df.column == 1], apply
"""

import pandas as pd 
import numpy as np

df = pd.read_csv("chipotle.tsv", sep = '\t')
def meta():
    print('-'*10)
    print(df.shape)
    print('-'*10)
    print(df.info())
    print('-'*10)
    print(df.columns)
    print('-'*10)
    print(df.index)

def most():
    # top 3 most ordered
    x=df.groupby('item_name').sum().sort_values(['quantity'], ascending=False)
    print(x.head(3))
    print(x.tail(5))
    print('-'*10)

def total():
    print(df.quantity.sum())
    #print('-'*10)

    # total revenue
    #print((df['quantity']*df['item_price']).sum())

    # num of orders
    # print('-'*10)
    # print(df.order_id.value_counts())
    # print(df.order_id.value_counts().count())

    # distinct items total
    # print('-'*10)
    # print(df.item_name.value_counts().count())

    #How many times was a Veggie Salad Bowl ordered?
    print('-'*10)
    print(df[df.item_name == 'Veggie Salad Bowl'].sum()['quantity'])

    # How many times did someone order more than one Canned Sod
    print('-',10)
    print(len(df[(df.item_name == "Canned Soda") & (df.quantity > 1)]))


def change_type():
    print(df.item_price.dtype)
    df.item_price = df.item_price.apply(lambda x:float(x[1:-1]))
    print(df.item_price.dtype)
    print(df.item_price.sum())

def filter():
    prices = [float(value[1 : -1]) for value in df.item_price]
    # reassign the column with the cleaned prices
    df.item_price = prices

    # delete the duplicates in item_name and quantity
    df_filtered = df.drop_duplicates(['item_name','quantity','choice_description'])

    print('1-'*10)
    print(df_filtered)

    # select only the products with quantity equals to 1
    df_one_prod = df_filtered[df_filtered.quantity == 1]
    print('2-'*10)
    print(df_one_prod)

    print('3-'*10) #25
    print(df_one_prod[df_one_prod['item_price']>10].item_name.nunique())

    print('4-'*10)
    print(df_one_prod[df_one_prod['item_price']>10])
    #print(df.query('item_price > 10').item_name.nunique())

    print('5-'*10)
    price_per_item = df_one_prod[['item_name', 'item_price']]
    print(price_per_item.sort_values(by='item_price', ascending=False).head(3))

def sort():
    print(df.item_name.sort_values().head(3))
    print(df.sort_values(by='item_name', ascending=False).head(3))


#meta()
#most()
total()
#change_type()
#filter()
#sort()
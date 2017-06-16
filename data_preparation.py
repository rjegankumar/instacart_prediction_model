# importing modules/ libraries
import pandas as pd
import numpy as np

orders_prior_df = pd.read_csv('Data/orders_prior_sample.csv')

order_products_prior_df = pd.read_csv('Data/order_products_prior_sample.csv')

grouped = order_products_prior_df.groupby('order_id', as_index = False)

grouped_data = pd.DataFrame()

grouped_data['order_id'] = grouped['order_id'].aggregate(np.mean)

def product_ids(group):
    l = []
    for e in group['product_id']:
        l.append(str(e))
    return ' '.join(l)

grouped_data['product_ids'] = grouped.apply(product_ids)

def add_to_cart_orders(group):
    l = []
    for e in group['add_to_cart_order']:
        l.append(str(e))
    return ' '.join(l)

grouped_data['add_to_cart_orders'] = grouped.apply(add_to_cart_orders)
print('First five rows of grouped_data:\n', grouped_data.head())

orders_prior_merged = pd.merge(orders_prior_df, grouped_data, on='order_id')
print('First five rows of orders_prior_merged:\n', orders_prior_merged.head())

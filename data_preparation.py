# importing modules/ libraries
import pandas as pd
import numpy as np

orders_prior_df = pd.read_csv('Data/orders_prior_sample.csv')
print('length of orders_prior_df:', len(orders_prior_df))

order_products_prior_df = pd.read_csv('Data/order_products_prior_sample.csv')
print('length of order_products_prior_df:', len(order_products_prior_df))

grouped = order_products_prior_df.groupby('order_id')

grouped_data = pd.DataFrame()

grouped_data['order_id'] = grouped['order_id'].aggregate(np.mean)

def product_ids(group):
    l = []
    ord_id = group['order_id']
    for e in group['product_id']:
        l.append(str(e))
    return ' '.join(l)

grouped_data['product_ids'] = grouped.apply(product_ids)
print('length of grouped_data:', len(grouped_data))

orders_prior_merged = pd.merge(orders_prior_df, grouped_data, on='order_id')
print('length of orders_prior_merged:', len(orders_prior_merged))

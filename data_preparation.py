# importing modules/ libraries
import pandas as pd
import numpy as np

# loading data
orders_prior_df = pd.read_csv('Data/orders_prior_sample.csv')
orders_train_df = pd.read_csv('Data/orders_train_sample.csv')
order_products_prior_df = pd.read_csv('Data/order_products_prior_sample.csv')
order_products_train_df = pd.read_csv('Data/order_products_train_sample.csv')

def merging_prods_orders(grouped_df):
    grp = pd.DataFrame()
    grp['order_id'] = grouped_df['order_id'].aggregate(np.mean)
    grp['product_ids'] = grouped_df.apply(product_ids)
    grp['add_to_cart_orders'] = grouped_df.apply(add_to_cart_orders)
    grp['reordered'] = grouped_df['reordered'].aggregate(np.mean)['reordered'].round()
    return grp

def product_ids(group):
    l = []
    for e in group['product_id']:
        l.append(str(e))
    return ' '.join(l)

def add_to_cart_orders(group):
    l = []
    for e in group['add_to_cart_order']:
        l.append(str(e))
    return ' '.join(l)

# merging prior product data with orders data
grouped_pr = order_products_prior_df.groupby('order_id', as_index = False)
grouped_data_pr = merging_prods_orders(grouped_pr)
print('First five rows of grouped_data_pr:\n', grouped_data_pr.head())

orders_prior_merged = pd.merge(orders_prior_df, grouped_data_pr, on='order_id')
print('First five rows of orders_prior_merged:\n', orders_prior_merged.head())
orders_prior_merged.to_csv('Data/orders_prior_merged.csv', index = False)

# merging train product data with orders data
grouped_tr = order_products_train_df.groupby('order_id', as_index = False)
grouped_data_tr = merging_prods_orders(grouped_tr)
print('First five rows of grouped_data_tr:\n', grouped_data_tr.head())

orders_train_merged = pd.merge(orders_train_df, grouped_data_tr, on='order_id')
print('First five rows of orders_train_merged:\n', orders_train_merged.head())
orders_train_merged.to_csv('Data/orders_train_merged.csv', index = False)

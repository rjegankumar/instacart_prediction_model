# importing modules/ libraries
import pandas as pd
import numpy as np

# loading data
orders_prior_df = pd.read_csv('Data/orders_prior_sample.csv')
print('\nFirst five rows of orders_prior_df:\n\n', orders_prior_df.head())
orders_train_df = pd.read_csv('Data/orders_train_sample.csv')
print('\nFirst five rows of orders_train_df:\n\n', orders_train_df.head())
order_products_prior_df = pd.read_csv('Data/order_products_prior_sample.csv')
order_products_train_df = pd.read_csv('Data/order_products_train_sample.csv')

def merging_prods_orders(grouped_df):
    grp = pd.DataFrame()
    grp['order_id'] = grouped_df['order_id'].aggregate(np.mean)
    grp['product_ids'] = grouped_df.apply(product_ids)
    return grp

def product_ids(group):
    l = []
    for e in group['product_id']:
        l.append(str(e))
    return ' '.join(l)

# merging prior product data with orders data
grouped_pr = order_products_prior_df.groupby('order_id', as_index = False)
grouped_data_pr = merging_prods_orders(grouped_pr)
print('\nFirst five rows of grouped_data_pr:\n\n', grouped_data_pr.head())

orders_prior_merged = pd.merge(orders_prior_df, grouped_data_pr, on='order_id')

# replacing NaNs in days since prior order with 0
orders_prior_merged.fillna(inplace = True, value = 0.0)

print('\nFirst five rows of orders_prior_merged:\n\n', orders_prior_merged.head())
orders_prior_merged.to_csv('Data/orders_prior_merged.csv', index = False)

# merging train product data with orders data
grouped_tr = order_products_train_df.groupby('order_id', as_index = False)
grouped_data_tr = merging_prods_orders(grouped_tr)
print('\nFirst five rows of grouped_data_tr:\n\n', grouped_data_tr.head())

orders_train_merged = pd.merge(orders_train_df, grouped_data_tr, on='order_id')

# replacing NaNs in days since prior order with 0
orders_train_merged.fillna(inplace = True, value = 0.0)

print('\nFirst five rows of orders_train_merged:\n\n', orders_train_merged.head())
orders_train_merged.to_csv('Data/orders_train_merged.csv', index = False)

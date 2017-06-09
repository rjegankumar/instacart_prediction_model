# importing modules/ libraries
import pandas as pd
import random
import numpy as np

# create sample of order products train data
n = 1384617
s = round(0.1 * n)
skip = sorted(random.sample(range(1,n), n-s))
order_products__train_sample_df = pd.read_csv('Data/order_products__train.csv', 
                                       index = 'order_Id', skiprows = skip)
order_products__train_sample_df.to_csv('Data/order_products__train_sample.csv')

# create sample of order products prior data
n = 32434489
s = round(0.1 * n)
skip = sorted(random.sample(range(1,n), n-s))
order_products__prior_sample_df = pd.read_csv('Data/order_products__prior.csv', 
                                       index = 'order_Id', skiprows = skip)
order_products__prior_sample_df.to_csv('Data/order_products__prior_sample.csv')

# create sample of orders data
prior_unique_ids = np.array(order_products__prior_sample_df.index.unique())
train_unique_ids = np.array(order_products__train_sample_df.index.unique())
match_ids = np.concatenate((prior_unique_ids, train_unique_ids), axis = 0)
order_sample_df = pd.read_csv('Data/orders.csv', index_col = 'order_id')
order_sample_df = order_sample_df.loc[match_ids,:]
order_sample_df.to_csv('Data/orders_sample.csv')
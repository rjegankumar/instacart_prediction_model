# importing modules/ libraries
import pandas as pd
import random

# create sample of order products train data
n = 1384617
s = round(0.1 * n)
skip = sorted(random.sample(range(1,n), n-s))
order_products__train_sample_df = pd.read_csv('Data/order_products__train.csv', 
                                       skiprows = skip)
order_products__train_sample_df.to_csv('Data/order_products__train_sample.csv', 
                                       index = False)

# create sample of order products prior data
n = 32434489
s = round(0.1 * n)
skip = sorted(random.sample(range(1,n), n-s))
order_products__prior_sample_df = pd.read_csv('Data/order_products__prior.csv', 
                                       skiprows = skip)
order_products__prior_sample_df.to_csv('Data/order_products__prior_sample.csv', 
                                       index = False)

# create sample of orders data
n = 3421083
s = round(0.1 * n)
skip = sorted(random.sample(range(1,n), n-s))
order_sample_df = pd.read_csv('Data/orders.csv', 
                                       skiprows = skip)
order_sample_df.to_csv('Data/orders_sample.csv', 
                                       index = False)
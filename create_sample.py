# importing modules/ libraries
import pandas as pd
import random
import numpy as np

# create a sample of prior orders
orders_df = pd.read_csv("Data/orders.csv")
s = round(3214874 * 0.1)
i = sorted(random.sample(range(1,3214874), s))
orders_df.loc[i,:].to_csv("Data/orders_prior_sample.csv", index = False)

# create a sample of train orders
s = round(131209 * 0.1)
j = sorted(random.sample(range(1,131209), s))
orders_df.loc[j,:].to_csv("Data/orders_train_sample.csv", index = False)

# create a sample of test orders
s = round(75000 * 0.1)
k = sorted(random.sample(range(1,75000), s))
orders_df.loc[k,:].to_csv("Data/orders_test_sample.csv", index = False)

# create a sample of prior order products
order_products_prior_df = pd.read_csv('Data/order_products__prior.csv', index_col = 'order_id')
order_products_prior_df.loc[orders_df.loc[i,:]['order_id'],:].to_csv("Data/order_products_prior_sample.csv", index = False)

# create a sample of train order products
order_products_train_df = pd.read_csv('Data/order_products__train.csv', index_col = 'order_id')
order_products_train_df.loc[orders_df.loc[j,:]['order_id'],:].to_csv("Data/order_products_train_sample.csv", index = False)

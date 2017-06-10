# importing modules/ libraries
import pandas as pd
import random
import numpy as np

# create a sample of prior orders
orders_df = pd.read_csv("Data/orders.csv")
s = round(3214874 * 0.1)
i = sorted(random.sample(list(orders_df[orders_df["eval_set"]=="prior"].index), s))
orders_df.loc[i,:].to_csv("Data/orders_prior_sample.csv", index = False)

# create a sample of train orders
s = round(131209 * 0.1)
j = sorted(random.sample(list(orders_df[orders_df["eval_set"]=="train"].index), s))
orders_df.loc[j,:].to_csv("Data/orders_train_sample.csv", index = False)

# create a sample of prior order products
order_products_prior_df = pd.read_csv('Data/order_products__prior.csv', index_col = 'order_id')
order_products_prior_df.loc[orders_df.loc[i,:]['order_id'],:].to_csv("Data/order_products_prior_sample.csv", index = False)

# create a sample of train order products
order_products_train_df = pd.read_csv('Data/order_products__train.csv', index_col = 'order_id')
order_products_train_df.loc[orders_df.loc[j,:]['order_id'],:].to_csv("Data/order_products_train_sample.csv", index = False)

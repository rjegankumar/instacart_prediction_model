# importing modules/ libraries
import pandas as pd
import random

# loading the data
aisles_df = pd.read_csv('Data/aisles.csv')
print(aisles_df.head())

departments_df = pd.read_csv('Data/departments.csv')
print(departments_df.head())

#n = 32434489
#s = round(0.1 * n)
#skip = sorted(random.sample(range(1,n), n-s))
order_products__prior_df = pd.read_csv('Data/order_products__prior.csv')
print(order_products__prior_df.head())

#n = 1384617
#s = round(0.1 * n)
#skip = sorted(random.sample(range(1,n), n-s))
order_products__train_df = pd.read_csv('Data/order_products__train.csv')
print(order_products__train_df.head())

#n = 3421083
#s = round(0.1 * n)
#skip = sorted(random.sample(range(1,n), n-s))
orders_df = pd.read_csv('Data/orders.csv')
print(orders_df.head())

products_df = pd.read_csv('Data/products.csv')
print(products_df.head())

sample_submission_df = pd.read_csv('Data/sample_submission.csv')
print(sample_submission_df.head())
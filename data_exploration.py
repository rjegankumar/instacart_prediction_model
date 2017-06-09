# importing modules/ libraries
import pandas as pd

# loading the data
aisles_df = pd.read_csv('Data/aisles.csv')
print(aisles_df.head())

departments_df = pd.read_csv('Data/departments.csv')
print(departments_df.head())

order_products__prior_df = pd.read_csv('Data/order_products__prior_sample.csv')
print(order_products__prior_df.head())

order_products__train_df = pd.read_csv('Data/order_products__train_sample.csv')
print(order_products__train_df.head())

orders_df = pd.read_csv('Data/orders_sample.csv')
print(orders_df.head())

products_df = pd.read_csv('Data/products.csv')
print(products_df.head())

sample_submission_df = pd.read_csv('Data/sample_submission.csv')
print(sample_submission_df.head())
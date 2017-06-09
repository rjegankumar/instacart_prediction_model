# importing modules/ libraries
import pandas as pd

# loading and exploring the data
aisles_df = pd.read_csv('Data/aisles.csv')
print("\nFirst five rows of aisles.csv:\n", aisles_df.head(), sep="\n")
print("\nDimensions of aisles.csv:\n", aisles_df.shape, sep="\n")
print("\nNull values in aisles.csv:\n", (aisles_df.isnull()).sum(), sep="\n")

departments_df = pd.read_csv('Data/departments.csv')
print("\nFirst five rows of departments.csv:\n", departments_df.head(), sep="\n")
print("\nDimensions of departments.csv:\n", departments_df.shape, sep="\n")
print("\nNull values in departments.csv:\n", (departments_df.isnull()).sum(), sep="\n")

prior_sample_df = pd.read_csv('Data/order_products__prior_sample.csv')
print("\nFirst five rows of order_products__prior_sample.csv:\n", 
      prior_sample_df.head(), sep="\n")
print("\nDimensions of order_products__prior_sample.csv:\n", 
      prior_sample_df.shape, sep="\n")
print("\nNull values in order_products__prior_sample.csv:\n", 
      (prior_sample_df.isnull()).sum(), sep="\n")

train_sample_df = pd.read_csv('Data/order_products__train_sample.csv')
print("\nFirst five rows of order_products__train_sample.csv:\n", 
      train_sample_df.head(), sep="\n")
print("\nDimensions of order_products__train_sample.csv:\n", 
      train_sample_df.shape, sep="\n")
print("\nNull values in order_products__train_sample.csv:\n", 
      (train_sample_df.isnull()).sum(), sep="\n")

orders_sample_df = pd.read_csv('Data/orders_sample.csv')
print("\nFirst five rows of orders_sample.csv:\n", 
      orders_sample_df.head(), sep="\n")
print("\nDimensions of orders_sample.csv:\n", 
      orders_sample_df.shape, sep="\n")
print("\nNull values in orders_sample.csv:\n", 
      (orders_sample_df.isnull()).sum(), sep="\n")

products_df = pd.read_csv('Data/products.csv')
print("\nFirst five rows of products.csv:\n", 
      products_df.head(), sep="\n")
print("\nDimensions of products.csv:\n", 
      products_df.shape, sep="\n")
print("\nNull values in products.csv:\n", 
      (products_df.isnull()).sum(), sep="\n")

sample_submission_df = pd.read_csv('Data/sample_submission.csv')
print("\nFirst five rows of sample_submission.csv:\n", 
      sample_submission_df.head(), sep="\n")
print("\nDimensions of sample_submission.csv:\n", 
      sample_submission_df.shape, sep="\n")
print("\nNull values in sample_submission.csv:\n", 
      (sample_submission_df.isnull()).sum(), sep="\n")
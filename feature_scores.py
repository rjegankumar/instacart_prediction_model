#importing modules/ libraries
import pandas as pd
import pprint
from sklearn.feature_selection import SelectKBest
import operator

# loading the merged prior data
prior_df = pd.read_csv('Data/orders_prior_merged.csv')

# feature list
feat_list = ['user_id',
            'order_number',
            'order_dow',
            'order_hour_of_day',
            'days_since_prior_order',
            'reordered']

# features and labels
features = prior_df[feat_list]
labels = prior_df['product_ids']
print(features.head())
print(labels.head())

# feature scores from SelectKBest
best_features = {}
selector = SelectKBest(k=6)
selector.fit(features, labels)
for i, s in enumerate(selector.scores_):
    best_features[feat_list[i]] = s
pprint.pprint(sorted(best_features.items(), key=operator.itemgetter(1), reverse=True))

'''
Output:
[('reordered', 1.2859232188693828),
 ('order_number', 1.1707303121136508),
 ('order_dow', 1.1694088148018937),
 ('order_hour_of_day', 1.0570877043125231),
 ('user_id', 1.0560200524619241),
 ('days_since_prior_order', 0.86511291673330581)]
 '''

import numpy as np 
import pandas as pd
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
import dvc.api

# Reading parameters from param.yaml 
params = dvc.api.params_show()

lr = params['learning_rate']
max_depth = params['learning_rate']
n_estimators = params['n_estimators']

# Read data 
features = pd.read_csv('../../data/processed/features.csv','\t')


# Create train and test split
X_train, X_test, y_train, y_test = train_test_split(\
    features.loc[:, features.columns != 'class'], \
        features['class'], test_size=0.33, random_state=42)

# Train gradient boosting algorithm
clf = GradientBoostingClassifier(n_estimators= n_estimators , learning_rate=lr,\
     max_depth= max_depth , random_state=0).fit(X_train, y_train)
clf.score(X_test, y_test)


with open('metrics.json', 'w') as metrics_file:
    metrics_dict = {
        'r2': score
    }

    metrics_file.write(json.dumps(metrics_dict))
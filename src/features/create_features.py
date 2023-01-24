import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)

# Reading the raw data file
iris_data = pd.read_csv('../../data/raw/iris.data', \
    names = [ 'sepal_length_cm','sepal_width_cm','petal_length_cm','petal_width_cm','class'])



# write the features file
iris_data[['sepal_length_cm','sepal_width_cm','class']].to_csv('../../data/processed/features.csv','\t')


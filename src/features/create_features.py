import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
iris_data = pd.read_csv('../data/iris.data', \
    names = [ 'sepal_length_cm','sepal_width_cm','petal_length_cm','petal_width_cm','class'])



# write the features file
iris_data.to_csv('../features','\t')


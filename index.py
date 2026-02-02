import pandas as pd
import numpy as np


# data = {   
#    'Product': ['Book', 'Pen', 'Notebook', 'Pencil', 'Eraser'],
#    'Price': [12.99, 1.99, 5.49, 0.99, 0.49],
#    'Stock': [100, 500, 200, 300, 400],
# }


# df = pd.DataFrame(data)


# gets the two first 2 rows in the dataframe
# print(df.head(2))

# gets the two last 2 rows in the dataframe
# print(df.tail(2))

# gets a summary statistics of the dataframe
# print(df.describe())

# gets information about the dataframe
# print(df.info())



df_csv = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data')

print(df_csv.head())
print(df_csv.describe())
print(df_csv.info())
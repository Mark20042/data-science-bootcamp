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



df_csv = pd.read_csv('penguins.csv')

# gets the two first 5 rows in the dataframe
print(df_csv.head())

# gets the shape of the dataframe
print(df_csv.shape)

# gets the count of unique values in the 'species' column
print(df_csv['species'].value_counts())


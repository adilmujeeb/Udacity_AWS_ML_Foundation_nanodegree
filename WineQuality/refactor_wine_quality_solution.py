# Refactor: Wine Quality Analysis

import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

# Renaming Columns
# Replace the spaces in the column labels with underscores to be able to 
# reference columns with dot notation. Here's one way you could've done it.

df.columns = [label.replace(' ', '_') for label in df.columns]
df.head()

# Analyzing Features

def numeric_to_buckets(df, column_name):
    median = df[column_name].median()
    for i, val in enumerate(df[column_name]):
        if val >= median:
            df.loc[i, column_name] = 'high'
        else:
            df.loc[i, column_name] = 'low' 

for feature in df.columns[:-1]:
    numeric_to_buckets(df, feature)
    print(df.groupby(feature).quality.mean(), '\n')
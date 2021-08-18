# Refactor: Wine Quality Analysis

import pandas as pd
df = pd.read_csv('winequality-red.csv', sep=';')
df.head()

# The csv file contains data about:
# 1. fixed acidity
# 2. volatile acidity
# 3. citric acid
# 4. residual sugar
# 5. chlorides
# 6. free sulfur dioxide
# 7. total sulfur dioxide
# 8. density
# 9. pH
# 10. sulphates
# 11. alcohol
# 12. quality
# 
# Renaming Columns
# Replace the spaces in the column labels with underscores to be able to 
# reference columns with dot notation. Here's one way you could've done it.

labels = list(df.columns)
for i in range(len(labels)):
    labels[i] = labels[i].replace(' ', '_')

# Best is to use below:
# df.columns = [label.replace(' ', '_') for label in df.columns]

df.columns = labels
df.head()

# Analyzing Features
# Observing the mean quality rating for the top and bottom half of each 
# feature. 

def feature_median(df, feature, name, f_median):
    for idx, f in enumerate(feature):
        if f >= f_median:
            df.loc[i, name] = 'high'
        else:
            df.loc[i, name] = 'low'
    df.groupby(name).quality.mean()

median_alcohol = df.alcohol.median()
feature_median(df, df.alcohol, 'alcohol', median_alcohol)

median_pH = df.pH.median()
feature_median(df, df.pH, 'pH', median_pH)

median_sugar = df.residual_sugar.median()
feature_median(df, df.residual_sugar, 'residual_sugar', median_sugar)

median_citric_acid = df.citric_acid.median()
feature_median(df, df.citric_acid, 'citric_acid', median_citric_acid)

# Generic solution 
## Analyzing Features

#def numeric_to_buckets(df, column_name):
#    median = df[column_name].median()
#    for i, val in enumerate(df[column_name]):
#        if val >= median:
#            df.loc[i, column_name] = 'high'
#        else:
#            df.loc[i, column_name] = 'low' 

#for feature in df.columns[:-1]:
#    numeric_to_buckets(df, feature)
#    print(df.groupby(feature).quality.mean(), '\n')
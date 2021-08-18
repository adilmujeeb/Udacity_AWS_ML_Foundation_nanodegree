# Wine Quality Analysis
# In this exercise, you'll refactor code that analyzes a wine quality dataset 
# taken from the UCI Machine Learning Repository (https://archive.ics.uci.edu/ml/datasets/wine+quality)
# Each row contains data on a wine sample, including several physicochemical 
# properties gathered from tests, as well as a quality rating evaluated by wine experts.
# The code first renames the columns of the dataset and then calculates some 
# statistics on how some features may be related to quality ratings. 
# Can you refactor this code to make it more clean and modular?

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

new_df = df.rename(columns={'fixed acidity': 'fixed_acidity',
                             'volatile acidity': 'volatile_acidity',
                             'citric acid': 'citric_acid',
                             'residual sugar': 'residual_sugar',
                             'free sulfur dioxide': 'free_sulfur_dioxide',
                             'total sulfur dioxide': 'total_sulfur_dioxide'
                            })
new_df.head()

# Better way of doing it to avoid typos

labels = list(df.columns)

labels[0] = labels[0].replace(' ', '_')
labels[1] = labels[1].replace(' ', '_')
labels[2] = labels[2].replace(' ', '_')
labels[3] = labels[3].replace(' ', '_')
labels[5] = labels[5].replace(' ', '_')
labels[6] = labels[6].replace(' ', '_')

# Another way of doing it 
labels2 = list(df.columns)
for i in range(len(labels2)):
    labels2[i] = labels2[i].replace(' ', '_')

df.columns = labels
df.head()

# Analyzing Features
# Now that your columns are ready, see how different features of this dataset 
# relate to the quality rating of the wine. A very simple way you could do this
# is by observing the mean quality rating for the top and bottom half of each 
# feature. The code below does this for four features. 
# It looks pretty repetitive right now. Can you make this more concise? 
# You might challenge yourself to figure out how to make this code more 
# efficient! But you don't need to worry too much about efficiency right 
# now - we will cover that more in the next section.

median_alcohol = df.alcohol.median()
for i, alcohol in enumerate(df.alcohol):
    if alcohol >= median_alcohol:
        df.loc[i, 'alcohol'] = 'high'
    else:
        df.loc[i, 'alcohol'] = 'low'
df.groupby('alcohol').quality.mean()

median_pH = df.pH.median()
for i, pH in enumerate(df.pH):
    if pH >= median_pH:
        df.loc[i, 'pH'] = 'high'
    else:
        df.loc[i, 'pH'] = 'low'
df.groupby('pH').quality.mean()

median_sugar = df.residual_sugar.median()
for i, sugar in enumerate(df.residual_sugar):
    if sugar >= median_sugar:
        df.loc[i, 'residual_sugar'] = 'high'
    else:
        df.loc[i, 'residual_sugar'] = 'low'
df.groupby('residual_sugar').quality.mean()

median_citric_acid = df.citric_acid.median()
for i, citric_acid in enumerate(df.citric_acid):
    if citric_acid >= median_citric_acid:
        df.loc[i, 'citric_acid'] = 'high'
    else:
        df.loc[i, 'citric_acid'] = 'low'
df.groupby('citric_acid').quality.mean()
import pandas as pd
import numpy as np

year0 = pd.read_csv('year0_cleaned_data.csv')
year1 = pd.read_csv('year1_cleaned_data.csv')

exclude_columns = [0,1,2,3,4,5,6]  # Example column numbers to exclude: 2, 4, 7

comparevalues = np.equal(year0.values, year1.values)
comparevalues[:, exclude_columns] = True  # Exclude specified columns from the comparison

rows, cols = np.where(comparevalues == False)

for row, col in zip(rows, cols):
    year0.iloc[row, col] = '{} --> {}'.format(year0.iloc[row, col], year1.iloc[row, col])

year0.to_csv('year1_differences.csv', index=False, header=True)

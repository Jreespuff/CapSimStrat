import pandas as pd
import numpy as np

data = pd.read_csv('year0_data.csv')

columns_to_clean = [2, 3, 6, 7, 8, 9, 10, 11, 14, 15]

for column_number in columns_to_clean:
    data.iloc[:, column_number] = data.iloc[:, column_number].fillna('').astype(str).str.extract(r'(\d+)')
    data.iloc[:, column_number] = pd.to_numeric(data.iloc[:, column_number], errors='coerce').fillna(np.nan).astype(float).astype(pd.Int32Dtype())


data.iloc[:, 0] = data.iloc[:, 0].str[4:]
data.iloc[:, 1] = data.iloc[:, 1].str[15:]
data.iloc[:, 4] = data.iloc[:, 4].str[13:]
data.iloc[:, 5] = data.iloc[:, 5].str[10:]
data.iloc[:, 12] = data.iloc[:, 12].str[19:]
data.iloc[:, 13] = data.iloc[:, 13].str[21:]
data.iloc[:, 16] = data.iloc[:, 16].str[17:]


data.to_csv('year0_cleaned_data.csv', index=False)


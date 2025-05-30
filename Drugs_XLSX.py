# pip install pandas openpyxl

import pandas as pd

df = pd.read_csv('drugs_filled.csv')

df.to_excel('drugs.xlsx', index=False, engine='openpyxl')
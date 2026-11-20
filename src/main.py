import pandas as pd

df = pd.read_excel('dataset-uci.xlsx', engine='calamine')

print(df)
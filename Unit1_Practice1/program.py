import pandas as pd

data = pd.read_csv("students.csv")

print(data.head())
print(data.shape)
print(data.columns)
print(data.describe())
print(data.isnull().sum())

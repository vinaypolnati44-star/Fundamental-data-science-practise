import pandas as pd
import numpy as np

data = {'Marks':[85,90,np.nan,95,100,30,110,np.nan,88,92]}
df = pd.DataFrame(data)

mean_value = df['Marks'].mean()
df['Marks'].fillna(mean_value, inplace=True)

filtered_df = df[(df['Marks']>=0) & (df['Marks']<=100)]

print(df)
print(filtered_df)

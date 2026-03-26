import pandas as pd
import matplotlib.pyplot as plt

data = {'Marks':[55,60,65,70,72,74,78,80,82,85,88,90,92,95,98]}
df = pd.DataFrame(data)

plt.hist(df['Marks'], bins=5)
plt.show()

plt.boxplot(df['Marks'])
plt.show()

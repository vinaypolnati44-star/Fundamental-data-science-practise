import pandas as pd
import matplotlib.pyplot as plt

data = {
 'Hours_Studied':[1,2,3,4,5,6,7,8,9,10],
 'Marks_Scored':[30,35,40,45,50,55,60,70,80,90]
}

df = pd.DataFrame(data)

plt.scatter(df['Hours_Studied'], df['Marks_Scored'])
plt.show()

print(df['Hours_Studied'].corr(df['Marks_Scored']))

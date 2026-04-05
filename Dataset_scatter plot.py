
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('EditableDataset_CSV.csv')
x=df['age']
y=df['rating']
x=x.dropna()
y=y.loc[x.index]

x=np.append(x,10)
y=np.append(y,10.5)

plt.scatter(x,y)
plt.xlabel('age')
plt.ylabel('rating')

plt.title("Negative Correlation with outlier")
plt.show()

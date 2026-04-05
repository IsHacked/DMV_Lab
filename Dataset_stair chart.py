import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df=pd.read_csv('EditableDataset_CSV.csv')
d = df.select_dtypes(include='number')

d = d.dropna()

for col in d.columns[0:]:  
    plt.step(df["freelancer_ID"], df[col], label=col)

plt.legend()
plt.title("Stair Graphs")
plt.ylabel("Characteristics")
plt.xlabel("freelancer_ID")
plt.show()
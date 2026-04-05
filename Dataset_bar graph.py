import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

df=pd.read_csv('EditableDataset_CSV.csv')

df.set_index("freelancer_ID", inplace=True)

df.plot(kind='bar')

plt.title('Bar Chart')
plt.xlabel('freelancer_ID')
plt.ylabel('Characteristics')
plt.show()
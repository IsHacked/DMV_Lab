import numpy as np
import pandas as pd

datas = {'Name':['A','B','C','D','E'], 
         'Age':[19,np.nan,21,19,20]}

df=pd.DataFrame(datas)

print("ORIGINAL DATASET:")
print(df)

df.dropna(how='any',inplace=True)

print("Modified dataset:")
print(df)

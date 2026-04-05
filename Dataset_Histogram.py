import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np

df=pd.read_csv('EditableDataset_CSV.csv')

numeric_df = df.select_dtypes(include='number')

for col in numeric_df.columns:
    plt.figure()
    plt.hist(numeric_df[col], bins=10)
    plt.title(f"Histogram of {col}")
    plt.xlabel(col)
    plt.ylabel("Frequency")

plt.show()
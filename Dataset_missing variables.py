import pandas as pd

df = pd.read_csv("EditableDataset_CSV.csv")

print("missing variables Locations (Represented by True):")
print(df.isnull())

print("Total number of missing values per column:")
print(df.isnull().sum())
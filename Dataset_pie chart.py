import pandas as pd
import matplotlib.pyplot as plt

#column-wise pie chart for String Valued / Categorical columns

df = pd.read_csv("EditableDataset_CSV.csv")

df.columns = df.columns.str.strip()

for col_name in df.columns:

    if pd.api.types.is_numeric_dtype(df[col_name]):
       pass
        
    else:
        plt.figure()
        counts = df[col_name].value_counts()

        plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
        plt.title(f"{col_name} Distribution")

plt.show()

"""
#row-wise pie chart

df = pd.read_csv("EditableDataset_CSV.csv")

df.columns = df.columns.str.strip()

numeric_df = df.select_dtypes(include='number')

numeric_df = numeric_df.dropna()

for i in range(len(numeric_df)):
    
    row_data = numeric_df.iloc[i] 

    plt.figure()
    plt.pie(row_data, labels=row_data.index, autopct='%1.1f%%')
    

    if "freelancer_ID" in df.columns:
        plt.title(f"Distribution for {df.loc[i, 'freelancer_ID']}")
    else:
        plt.title(f"Row {i}")

plt.show()
"""


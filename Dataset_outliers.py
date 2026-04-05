import pandas as pd

df = pd.read_csv("EditableDataset_CSV.csv")

numeric_df = df.select_dtypes(include='number')
print("Outliers in the dataset are: ")

for col in numeric_df.columns:
    numeric_df[col] = numeric_df[col].fillna(df[col].mean())
    q1 = numeric_df[col].quantile(0.25)
    q3 = numeric_df[col].quantile(0.75)
    IQR = q3 - q1

    lowerQ = q1 - 1.5 * IQR
    upperQ = q3 + 1.5 * IQR

    outliers = numeric_df[(numeric_df[col] < lowerQ) | (numeric_df[col] > upperQ)]

    print(f"Column {col}:\n", outliers)
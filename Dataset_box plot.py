import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('EditableDataset_CSV.csv')

df.boxplot()

plt.xlabel("Characteristics")
plt.title("Box plot of Freelancer's dataset")
plt.show()

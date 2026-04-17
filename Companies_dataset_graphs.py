"""
    Pie chart (Employees and Companies names)
    
"""
    
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("company_dataset.csv")
df.dropna()
x=df['employees']

plt.figure()
counts = x.value_counts()
plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
plt.title(f"Employees Distribution")

plt.show()


"""
    Funnel chart (Rating wise)

"""




"""
    Bar chart (Companies and year wise)

"""

df=pd.read_csv('company_dataset_First_100.csv')

x=df['name']
y=df['ratings']

plt.bar(x,y)
plt.title('Bar Chart')
plt.xlabel('Company names')
plt.ylabel('Rating')
plt.show()

"""
    Line chart (Companies and ctype)
    
"""

"""
df=pd.read_csv('company_dataset_First_100.csv')

x=df['name']
y=df['years']

plt(x,y)

plt.xlabel('Company names')
plt.ylabel('Years')
plt.title('Line chart')
plt.show()
"""

"""
    Histogram (Companies and Review count)
    
"""

df=pd.read_csv('company_dataset_First_100.csv')

x=df['review_count']

plt.hist(x)
plt.xlabel(x)
plt.ylabel('No: of companies')
plt.show()
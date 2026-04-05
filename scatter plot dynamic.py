import matplotlib.pyplot as plt 
import numpy as np

x=[]
y=[]

n=int(input("Enter no: of data points"))

for i in range (n):
    x.append(input("Enter x data point:"))
    y.append(int(input("Enter y data point")))

plt.scatter(x,y)
plt.title('Scatter plot')
plt.xlabel(x)
plt.ylabel(y)
plt.show()
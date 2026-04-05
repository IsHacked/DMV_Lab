import matplotlib.pyplot as plt 
import numpy as np

x=[]
y=[]

n=int(input("Enter no: of data points"))

for i in range (n):
    x.append(input("Enter x(label) data point:"))
    y.append(int(input("Enter y(size) data point")))

plt.pie(y,labels=x)
plt.title('pie chart')
plt.show()
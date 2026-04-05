import matplotlib.pyplot as plt 
import numpy as np

x=[]
y=[]

n=int(input("Enter no: of data points"))

for i in range (n):
    x.append(input("Enter x data point:"))
    y.append(int(input("Enter y data point")))

print(x)
print(y)

plt.bar(x,y)
plt.xlabel(x)
plt.ylabel(y)
plt.title('Bar chart')
plt.show()
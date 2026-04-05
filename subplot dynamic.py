import matplotlib.pyplot as plt 
import numpy as np

x=[]
y=[]
a=[]
b=[]

plt.subplot(2,1,1)
n=int(input("Enter no: of data points in first subplot"))
for i in range (n):
    x.append(int(input("Enter x data point:")))
    y.append(int(input("Enter y data point")))
plt.plot(x,y)
plt.title("squares")

plt.subplot(2,1,2)
n=int(input("Enter no: of data points in second subplot"))
for i in range (n):
    a.append(int(input("Enter x data point:")))
    b.append(int(input("Enter y data point")))
plt.plot(a,b)
plt.title("cubes")

plt.tight_layout()
plt.show()


import matplotlib.pyplot as plt 
import numpy as np

age=[]

n=int(input("Enter no: of data points:"))

for i in range(n):
    age.append(int(input("Enter age: ")))

plt.hist(age)
plt.xlabel('Age')
plt.ylabel('No: of students')
plt.title('Histogram of Age vs no of students')
plt.show()
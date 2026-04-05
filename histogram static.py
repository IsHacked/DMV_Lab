import matplotlib.pyplot as plt 
import numpy as np

age=[19,20,21,22,23,19,20,21,20,21,20]

plt.hist(age)
plt.xlabel('Age')
plt.ylabel('No: of students')
plt.title('Histogram of Age vs no of students')
plt.show()
import matplotlib.pyplot as plt 
import numpy as np

x=['A','B','C','D','E']
y=[10,20,15,25,30]

plt.pie(y,labels=x)
plt.title('pie chart')
plt.show()
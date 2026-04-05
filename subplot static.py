import matplotlib.pyplot as plt 
import numpy as np

plt.subplot(2,1,1)
plt.plot([1,2,3],[1,4,9])
plt.title("squares")

plt.subplot(2,1,2)
plt.plot([1,2,3],[1,8,27])
plt.title("cubes")

plt.tight_layout()
plt.show()
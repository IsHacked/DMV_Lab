import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y=[19,20,25,10,30]

plt.plot(x,y,marker='o')

plt.xlabel("Independent variable(x)")
plt.ylabel("Dependent variable(y)")

plt.title("X-Y data plot")

plt.grid(True)
plt.show()
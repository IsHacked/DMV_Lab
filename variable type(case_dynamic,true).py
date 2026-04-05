import matplotlib.pyplot as plt

x=[]
y=[]

n=int(input("Enter no: of x data points"))

for i in range (n):
    x.append(input("Enter x data point:"))
    y.append(int(input("Enter y data point")))

print(x)
print(y)

plt.plot(x,y,marker='o')

plt.xlabel("Independent variable(x)")
plt.ylabel("Dependent variable(y)")

plt.title("X-Y data plot")

plt.grid(True)
plt.show()
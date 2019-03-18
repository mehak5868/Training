import matplotlib.pyplot as plt

x=[1,2,3,4,5]
y1=(n for n in x)
y2=(n*n for n in x)
y3=(n*n*n for n in x)

plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.show()


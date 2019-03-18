import matplotlib.pyplot as plt

"""y=[5,7,9,11,13]
plt.plot(y)
plt.show()"""

"""x=list(range(10))
y=(n**2 for n in x )
plt.plot(y)
plt.show()"""

x=list(range(1,11))
y1=[n for n in x]
y2=[n*n for n in x]
y3=[n*n*n for n in x]

plt.plot(x,y1,"--")
plt.plot(x,y2,label="y2")
plt.plot(x,y3,label="y3")

plt.legend()
plt.xlabel("x-Axis")
plt.ylabel("y-Axis")
plt.title("PolynomialGraphs")
#plt.savefig("Polynomial Graphs.png")
plt.show()
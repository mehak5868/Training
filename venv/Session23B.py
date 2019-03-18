import numpy as np

"""arr = np.loadtxt("data.txt")
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.reshape)"""

arr = np.genfromtxt("CityTemp.csv", delimiter=",")
print(arr)

print(arr.shape)
print(arr.ndim)


np.savetxt("CityTemps1.csv",arr, delimiter=",")
print(">> File Created")


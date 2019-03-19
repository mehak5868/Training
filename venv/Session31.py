
import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt

data = pd.read_csv("advertising.csv")
# print(data)
# print(data["TV"])
# print(data["TV"].values)
# print(data["Sales"].values)

X = data["TV"].values
Y = data["Sales"].values

# print(X)
# print(Y)

##############
data = stats.linregress(X, Y)
# print(data[0]) # b1
# print(data[1]) # b0

b0 = data[1]
b1 = data[0]

# Y = b0 + b1X

Y1 = []

for x in X:
    y = b0 + (b1*x)
    Y1.append(y)
print(Y1)


#plt.xlabel("X")
#plt.ylabel("Y")
#plt.grid(True)
#plt.plot(X,Y,"o",X,Y1)
#plt.show()
X=X.reshape(len(X),1)
Y=X.reshape(len(Y),1)

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
regression = LinearRegression()
regression.fit(X,Y)
y2= regression.predict(X)
b0=regression.intercept_
b1=regression.coef_

r2err=r2_score(Y,y2)
print("Squared error :",r2err)
plt.scatter(X,Y,color="black")
plt.scatter(X,y2,color="blue")
plt.show()





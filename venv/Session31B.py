import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
data = pd.read_csv("StudentPredict.csv")
X=data["Class"].values
Y=data["Marks"].values

data = stats.linregress(X,Y)
b0=data[1]
b1=data[0]

y1=[]

for x in X:
    y = b0+(b1*x)
    y1.append(y)
print(y1)
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.plot(X,Y,"o",X,y1)
#plt.show()





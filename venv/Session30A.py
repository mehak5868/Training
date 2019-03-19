from sklearn import tree
import pandas as pd
#X=[1,2,3,4,5]
#Y=[2,4,5,4,5]
data = pd.read_csv("advertising.csv")
X = data["TV"].values
Y = data["Sales"].values
x1=0
y1=0
#mean of X
for x in X :
    x1=x1+x
MX=x1//len(X)
print("mean of X:",MX)

#mean of Y
for y in Y :
    y1=y1+y
MY=y1//len(Y)
print("mean of Y:",MY)

#X-MX
S =[]
for x in X :
    x1 = x - MX
    S.append(x1)
print("X-MX :",S)

#Y-MY
S1 =[]
for y in Y :
    y1 = y -MY
    S1.append(y1)
print("Y-MY :",S1)

#square of (X-MX)
S2 =[]
for mx in S :
    x1 = mx **2
    S2.append(x1)
print("Sq(X-MX):",S2)

#(X-MX)(Y-MY)
S3 =[]
for x in range (0,len(S)):
    S3.append(S[x]*S1[x])
print("(X-MX)(Y-MY):",S3)

#Sum of square of (X-MX)
w=0
for s in S2:
    w= w + s
print("Sum of square of (X-MX):",w)

#Sum of (X-MX)(Y-MY)
w1=0
for s in S3 :
    w1 = w1 + s
print("Sum of (X-MX)(Y-MY):",w1)

b1 = w1/w
print("b1:",b1)

b0 = MY - (b1*MX)
print("b0:",b0)





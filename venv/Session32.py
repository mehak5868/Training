import pandas as pd
import math
data = pd.read_csv("Play.csv")
#Entropy of play
x=data["play"].values
p=len(x) #lenght of list
print(p)
a=0
b=0
for x1 in x:
    if x1 == "yes" :
        a=a+1
    elif x1 == "no":
        b=b+1

print("yes:",a)
print("no:",b)

l = math.log2(a/p)#log2(p(yes))
l1 = math.log2(b/p)#log2(p(no))
print("yes:",l,"no:",l1)

ep = -a/p * l - b/p* l1
print("E(p):",ep)

#entropy of outlook
def ol():
    y = data["outlook"].values
    a1 = 0
    b1 = 0
    c1 = 0
    sunny = []
    overcast = []
    rainy = []
    for i in range (0,len(y)) :
        if y[i] == "sunny" :
            a1 = a1 + 1
            sunny.append(x[i])
        elif y[i] == "overcast":
            b1 = b1 + 1
            overcast.append(x[i])
        elif y[i] == "rainy":
            c1 = c1 + 1
            rainy.append(x[i])
    print("Sunny :",a1 , ",Overcast :",b1,",Rainy :", c1)
    print("Sunny :",sunny)
    print("Overcast :",overcast)
    print("Rainy :",rainy)

    sp = a1 / p #Probability of sunny
    op = b1 / p #Probability of overcast
    rp = c1 / p #Probability of rainy
    #entroy of sunny
    a2 = 0
    b2 = 0
    for j in sunny :
        if j == "yes":
            a2 = a2 + 1
        elif j == "no":
            b2 = b2 + 1

    print("Sunny :- Yes :",a2,"no :",b2)

    l3 = math.log2(a2/a1)
    l4 = math.log2(b2/a1)

    es = -a2/a1 * l3 - b2/a1*l4
    print("Entropy of Sunny :",es)
    #entropy of overcast
    a3 = 0
    b3 = 0
    for j1 in overcast :
        if j1 == "yes":
            a3 = a3 + 1
        elif j1 == "no":
            b3 = b3 + 1
    print("Overcast:- Yes :",a3,"no :",b3)
    l5 = math.log(a3/b1,2)
    #l6 = math.log2(0)
    eo = -a3/b1 * l5 - 0
    print("Entropy of Overcast :",eo)

    #entropy of rainy
    a4 = 0
    b4 = 0
    for j in rainy :
        if j == "yes":
            a4 = a4 + 1
        if j == "no":
            b4 = b4 + 1
    print("Rainy:- Yes :",a4,"no :",b4)

    l6 = math.log2(a4/c1)
    l7 = math.log2(b4/c1)

    er = -a4/c1 * l6 -b4/c1*l7
    print("Entropy of rainy :",er)

    #information from outlook
    i = sp * es + op * eo + rp * er
    print("Info(outlook) :",i)

    #information gained from outlook
    go = ep - i
    print("Gained value(outlook):",go)
ol()

#entropy of temp
def temp ():
    z = data["temp"].values
    a1 = 0
    b1 = 0
    c1 = 0
    hot = []
    mild = []
    cool= []
    for i in range (0,len(z)) :
        if z[i] == "hot" :
            a1 = a1 + 1
            hot.append(x[i])
        elif z[i] == "mild":
            b1 = b1 + 1
            mild.append(x[i])
        elif z[i] == "cool":
            c1 = c1 + 1
            cool.append(x[i])
    print("hot :",a1 , ",mild :",b1,",cool :", c1)
    print("hot :",hot)
    print("mild :",mild)
    print("cool :",cool)

    sp = a1 / p #Probability of hot
    op = b1 / p #Probability of mild
    rp = c1 / p #Probability of cool
    #entroy of hot
    a2 = 0
    b2 = 0
    for j in hot :
        if j == "yes":
            a2 = a2 + 1
        elif j == "no":
            b2 = b2 + 1

    print("hot:- Yes :",a2,"no :",b2)

    l3 = math.log2(a2/a1)
    l4 = math.log2(b2/a1)

    es = -a2/a1 * l3 - b2/a1*l4
    print("Entropy of hot :",es)
    #entropy of mild
    a3 = 0
    b3 = 0
    for j1 in mild :
        if j1 == "yes":
            a3 = a3 + 1
        elif j1 == "no":
            b3 = b3 + 1
    print("mild:- Yes :",a3,"no :",b3)
    l5 = math.log(a3/b1,2)
    l8 = math.log2(b3/b1)
    eo = -a3/b1 * l5 - b3/b1 *l8
    print("Entropy of mild :",eo)

    #entropy of cool
    a4 = 0
    b4 = 0
    for j in cool:
        if j == "yes":
            a4 = a4 + 1
        if j == "no":
            b4 = b4 + 1
    print("cool:- Yes :",a4,"no :",b4)

    l6 = math.log2(a4/c1)
    l7 = math.log2(b4/c1)

    er = -a4/c1 * l6 -b4/c1*l7
    print("Entropy of cool :",er)

    #information from outlook
    i = sp * es + op * eo + rp * er
    print("Info(temp) :",i)

    #information gained from outlook
    go = ep - i
    print("Gained value (temp):",go)

temp()

def humidity ():
    f = data["humidity"].values
    a5 = 0
    b5 = 0
    true=[]
    false =[]
    for i in range(0,len(f)):
        if f[i] == "high" :
            a5 = a5 + 1
            true.append(x[i])
        elif f[i] == "normal":
            b5 = b5 +1
            false.append (x[i])
    print ("high :",a5)
    print("normal :", b5)
    tp = a5 / p
    fp = b5 / p
    #entropy of high :
    a6 = 0
    b6 = 0
    for i1 in true :
        if i1 == "yes":
            a6 =a6 + 1
        elif i1 == "no":
            b6 = b6 + 1

    l9 = math.log2(a6/a5)
    l0 = math.log2(b6/a5)
    et = -a6/a5 *l9 - b6/a5 *l0
    print("Entropy of high :",et)

    #entropy of normal :
    a7 = 0
    b7 = 0
    for j in false :
        if j == "yes":
            a7 = a7 + 1
        elif j == "no":
            b7 = b7 + 1
    l11 = math.log2(a7/b5)
    l12 = math.log2(b7/b5)
    ef = - a7 / b5 * l11 - b7 /b5 * l12
    print("entropy of normal :",ef)

    iw = tp * et + fp * ef
    print("info (humidity):",iw)

    gw = ep - iw
    print("gained value (humidity):",gw)

humidity()

def windy ():
    g = data["windy"].values
    a5 = 0
    b5 = 0
    true=[]
    false =[]
    for i in range(0,len(g)):
        if g[i] == "t" :
            a5 = a5 + 1
            true.append(x[i])
        elif g[i] == "f":
            b5 = b5 +1
            false.append (x[i])
    print ("true :",a5)
    print("false :", b5)
    tp = a5 / p
    fp = b5 / p
    #entropy of true :
    a6 = 0
    b6 = 0
    for i1 in true :
        if i1 == "yes":
            a6 =a6 + 1
        elif i1 == "no":
            b6 = b6 + 1

    l9 = math.log2(a6/a5)
    l0 = math.log2(b6/a5)
    et = -a6/a5 *l9 - b6/a5 *l0
    print("Entropy of false :",et)

    #entropy of false:
    a7 = 0
    b7 = 0
    for j in false :
        if j == "yes":
            a7 = a7 + 1
        elif j == "no":
            b7 = b7 + 1
    l11 = math.log2(a7/b5)
    l12 = math.log2(b7/b5)
    ef = - a7 / b5 * l11 - b7 /b5 * l12
    print("entropy of false :",ef)

    iw = tp * et + fp * ef
    print("info (windy):",iw)

    gw = ep - iw
    print("gained value (windy):",gw)
windy()


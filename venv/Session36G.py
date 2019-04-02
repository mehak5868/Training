import pandas as pd
from scipy import stats
import matplotlib.pyplot as plt
import numpy as np
def AcademicsAnalysis ():
    data = pd.read_csv("Example.csv")
    data1 = pd .read_csv("Example2.csv")
    Standards = data ["Standard"].values
    English=data["English"].values
    Maths=data["Maths"].values
    Hindi=data["Hindi"].values
    Punjabi = data["Punjabi"].values
    SST = data["SST"].values
    Science =data["Science"].values

    Standard1 =data1["Standard"].values
    English1 = data1["English"].values
    Math1 = data1["Math"].values
    Hindi1 = data1["Hindi"].values
    Punjabi1 = data1["Punjabi"].values
    Evs = data1["Evs"].values

    Eng =[]
    Math =[]
    Hin =[]
    Pun =[]
    Stand =[]

    for e in English1 :
        Eng.append(e)
    for e in English:
        Eng.append(e)
    print(Eng)

    for m in Math1:
        Math.append(m)
    print(Maths)
    for m in Maths:
        Math.append(m)

    for h in Hindi1:
        Hin.append(h)
    for h in Hindi:
        Hin.append(h)

    for p in Punjabi1:
        Pun.append(p)
    for p in Punjabi :
        Pun.append(p)

    for s in Standard1:
        Stand.append(s)
    for s in Standards:
        Stand.append(s)
    print(Stand)

    Data1 =stats.stats.linregress(Stand , Eng )

    #b0 = Data1[1]
    #b1 = Data1[0]

    # Y = b0 + b1X

    Y1 = []

    #for x in Stand :
        #y = b0 + (b1 * x)
        #Y1.append(y)
    #print(Y1)

    #plt.xlabel("X")
    #plt.ylabel("Y")
    #plt.grid(True)
    #plt.plot(Stand, Y1)
    #plt.show()


    X= np.array(Stand)
    Y = np.array(Eng)

    Stand = X.reshape(len(X), 1)
    Eng= Y.reshape(len(Y), 1)

    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import r2_score, mean_absolute_error
    regression = LinearRegression()
    regression.fit(Stand, Eng)
    y2 = regression.predict(Stand)
    print(y2)
    b0 = regression.intercept_
    b1 = regression.coef_

    r2err = r2_score(Eng, y2)
    # mbe = mean_absolute_error(Y,y2)
    print("Squared error :", r2err)
    # print("mean absolute error :",mbe)
    x = np.arange(10)
    plt.xticks(x, labels=Stand)
    plt.plot(Stand,Eng, color="black")
    plt.plot(Stand, y2, color="blue")
    plt.scatter(Stand, Eng, color="black")
    plt.scatter(Stand, y2, color="blue")
    plt.show()


AcademicsAnalysis()

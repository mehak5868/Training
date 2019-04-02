import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
global MeanSports
global MeanActivity
def SportsAnalysis():

    data =pd.read_csv("Example1.csv")

    Gold = data["golds"].values
    Silver =data["silvers"].values
    Bronze =data["bronzes"].values
    print(Gold)
    print(Silver)
    print(Bronze)
    allOverScore =[]
    g1 = 0
    for g in Gold :
        g1 =g1 + g
    g2 =g1*90
    meanGold=g2/len(Gold)
    allOverScore.append(meanGold)

    s1 =0
    for s in Silver:
        s1 =s1+s
    s2 = s1*60
    meanSilver=s2/len(Silver)
    allOverScore.append(meanSilver)

    b1=0
    for b in Bronze:
        b1 =b1+b
    b2 = b1 *30
    meanBronze=b2/len(Bronze)
    allOverScore.append(meanBronze)

    print(allOverScore)
    ms = 0

    for i in allOverScore:
        ms = ms + i
    MeanSports = ms/len(allOverScore)
    print(MeanSports)

    Medals  = ["Gold","Silver","Bronze"]
    plt.plot(Medals,allOverScore)
    plt.bar(Medals,allOverScore)
    x = np.arange(4)
    plt .xticks(x , labels = Medals)
    plt.legend(Medals)
    plt.show()
SportsAnalysis()

def ActivityAnalysis():

    data =pd.read_csv("Example1.csv")

    Gold = data["golds"].values
    Silver =data["silvers"].values
    Bronze =data["bronzes"].values
    print(Gold)
    print(Silver)
    print(Bronze)
    allOverScore =[]
    g1 = 0
    for g in Gold :
        g1 =g1 + g
    g2 =g1*90
    meanGold=g2/len(Gold)
    allOverScore.append(meanGold)

    s1 =0
    for s in Silver:
        s1 =s1+s
    s2 = s1*60
    meanSilver=s2/len(Silver)
    allOverScore.append(meanSilver)

    b1=0
    for b in Bronze:
        b1 =b1+b
    b2 = b1 *30
    meanBronze=b2/len(Bronze)
    allOverScore.append(meanBronze)

    print(allOverScore)
    ms = 0

    for i in allOverScore:
        ms = ms + i
    MeanActivity = ms/len(allOverScore)
    print(MeanActivity)

    Medals  = ["Gold","Silver","Bronze"]
    plt.plot(Medals,allOverScore)
    plt.bar(Medals,allOverScore)
    x = np.arange(4)
    plt .xticks(x , labels = Medals)
    plt.legend(Medals)
    plt.show()

ActivityAnalysis()

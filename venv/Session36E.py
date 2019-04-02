import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

OverAll=[]
data = pd.read_csv("Example.csv")
data1 = pd.read_csv("Example2.csv")
English = data["English"].values
Math = data["Maths"].values
Hindi = data["Hindi"].values
Punjabi = data["Punjabi"].values
SST = data["SST"].values
Science = data["Science"].values

English1 = data1["English"].values
Math1 = data1["Math"].values
Hindi1 = data1["Hindi"].values
Punjabi1 = data1["Punjabi"].values
Evs = data1["Evs"].values
allOverMarks = []
e1 = 0
e2 = 0
for e in English:
    e1 = e1 + e
for e in English1:
    e2 = e2 + e
e3 = e1 + e2
allOverEng = e3 / (len(English) + len(English1))
print(allOverEng)
allOverMarks.append(allOverEng)

m1 = 0
m2 = 0
for m in Math:
    m1 = m1 + m
for m in Math1:
    m2 = m2 + m
m3 = m1 + m2
allOverMath = m3 / (len(Math) + len(Math1))
print(allOverMath)
allOverMarks.append(allOverMath)

h1 = 0
h2 = 0
for h in Hindi:
    h1 = h1 + h
for h in Hindi1:
    h2 = h2 + h
h3 = h1 + h2
allOverHindi = h3 / (len(Hindi) + len(Hindi1))
print(allOverHindi)
allOverMarks.append(allOverHindi)

p1 = 0
p2 = 0
for p in Punjabi:
    p1 = p1 + p
for p in Punjabi1:
    p2 = p2 + p
p3 = p1 + p2
allOverPunjabi = p3 / (len(Punjabi) + len(Punjabi1))
allOverMarks.append(allOverPunjabi)

ss1 = 0
for ss in SST:
    ss1 = ss1 + ss
alloverSST = ss1 / len(SST)
allOverMarks.append(alloverSST)

s1 = 0
for s in Science:
    s1 = s1 + s
allOverSci = s1 / len(Science)
allOverMarks.append(allOverSci)

ev1 = 0
for e in Evs:
    ev1 = ev1 + e
allOverEvs = ev1 / len(Evs)
allOverMarks.append(allOverEvs)
print(allOverMarks)

ma = 0
for i in allOverMarks:
    ma = ma + i

MeanAcadmeics = ma / len(allOverMarks)
print(MeanAcadmeics)
OverAll.append(MeanAcadmeics)

data = pd.read_csv("Example1.csv")

Gold = data["golds"].values
Silver = data["silvers"].values
Bronze = data["bronzes"].values
print(Gold)
print(Silver)
print(Bronze)
allOverScore = []
g1 = 0
for g in Gold:
    g1 = g1 + g
g2 = g1 * 90
meanGold = g2 / len(Gold)
allOverScore.append(meanGold)

s1 = 0
for s in Silver:
    s1 = s1 + s
s2 = s1 * 60
meanSilver = s2 / len(Silver)
allOverScore.append(meanSilver)

b1 = 0
for b in Bronze:
    b1 = b1 + b
b2 = b1 * 30
meanBronze = b2 / len(Bronze)
allOverScore.append(meanBronze)

print(allOverScore)
ms = 0

for i in allOverScore:
    ms = ms + i
MeanSports = ms / len(allOverScore)
print(MeanSports)
OverAll.append(MeanSports)
print(OverAll)

Label = ["Academics ","Sports"]
plt.plot(Label,OverAll)
plt.bar(Label,OverAll)
x = np.arange(4)
plt .xticks( x, labels = Label)

plt.show()


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

df = pd.read_csv("Students.csv")
"""print(df)"""

"""plt.figure(figsize=(30,20))
sb.countplot(y=df.Nationality, palette="Set2")
plt.show()"""

w1 = 1
w2 = 1
w3 = 1
w4 = 3
w5 = 4

df["GK_Shot_Stopper"] = (w1*df.GK_Positioning + w2*df.GK_Diving + w3*df.GK_Kicking + w4*df.GK_Handling + w5*df.GK_Reflexes)
# print(df["GK_Shot_Stopper"])

sortedDf = df.sort_values("GK_Shot_Stopper")
# print(sortedDf)
print(sortedDf.head(5))
print()
print(sortedDf.tail(5))

filteredDf = sortedDf.tail(5)
plt.figure(figsize=(15,10))
sb.countplot(x="Nationality", data=filteredDf)
plt.show()
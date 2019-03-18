import numpy as np
import pandas as pd

table = np.genfromtxt("CityTemp.csv",delimiter=",")
print(table[0][1])
print("=====")
"""table = pd.read_csv("CityTemp.csv")
print(table)
print(table["Year"])"""
table = pd.read_csv("CityTemp.csv")
#print(table)

print("====")

#print(table["Year"])

print("====")
av=(table.iloc[0][4]+table.iloc[0][2]+table.iloc[0][3])/3
print(table.iloc[0][4])
print(table.iloc[0][2])
print(table.iloc[0][3])
print(av)


#print(table.iloc[1][2])


print("=====")
#print(table.iloc[1:5])
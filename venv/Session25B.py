import numpy as np
import matplotlib.pyplot as plt

sales ={"2015":50,"2016":30,"2017":120,"2018":90}
for i , key in enumerate(sales):
    plt.bar(i,sales[key]) #bar graphs

x=np.arange(len(sales))
plt.xticks(x,sales.keys())
plt.xlabel("Years")
plt.ylabel("Sales")
plt.title("Maruti sales")
plt.legend(sales)
plt.show()
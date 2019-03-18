import matplotlib.pyplot as plt

plt.figure(figsize=(6,6))

jobs=[120,50,60]
domains=["IT","Marketing","Accounts"]

plt.pie(jobs,labels=domains) #piechart

plt.legend()
plt.show()

#SVM - support vector machine
#Naive Bayes - Face recognition , Weather , Email filtering, News filtering , diagnostic
#types of Naive Byes :

from sklearn.naive_bayes import GaussianNB
import numpy as np

FEATURES=np.array([[100,100],[150,110],[1200,1300],[180,150],[800,1000],[200,180],[1000,1200],[1500,1500]])
LABELS =np.array([0,0,1,0,1,0,1,1])
model=GaussianNB()
model.fit(FEATURES,LABELS)

dataToPredict =[1300,1100]
output = model.predict([dataToPredict])
print("Prediction :",output)

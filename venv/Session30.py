#machine Learning -  scki
#meduim.com
from sklearn import tree
data=[[100,100],[180,150],[150,110],[200,180],[800,1000],[1000,1200],[1200,1300],[1500,1500]]
outputs=[0,0,0,0,1,1,1,1]
clf=tree.DecisionTreeClassifier()
clf.fit(data,outputs)
input=[[100,120]]
print(clf.predict(input))
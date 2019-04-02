from sklearn.datasets import load_iris
from sklearn import tree
import graphviz
irisData = load_iris()
print(irisData)
"""print("==========Data=========")
print (irisData.data)
print("========Target=========")
print(irisData.target)
print("=========Names=========")
print(irisData.target_names)"""

classifer = tree.DecisionTreeClassifier()
classifer.fit(irisData.data , irisData.target)

inputData = [7.7, 3.8, 6.7, 2.2]
predicted = classifer.predict([inputData])
print("Flower Predicted :",predicted)
print("Flower Predicted :",predicted[0])
print("Flower Predicted :",irisData.target_names[predicted[0]])

""""data =tree.export_graphviz(classifer,out_file=None)
graph = graphviz.Source(data)
graph.render("IRIS DATA-SET TREE")
graph.view()"""



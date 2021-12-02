import pandas as pd
from sklearn.datasets import load_iris
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics

iris=load_iris()
print("target names ",iris.target_names)


Xtrain,Xtest,Ytrain,Ytest=train_test_split(iris.data,iris.target)

knn=KNeighborsClassifier(n_neighbors=1)
ypred=knn.fit(Xtrain,Ytrain).predict(Xtest)
print("Accuracy :",metrics.accuracy_score(Ytest,ypred))

print("First few predictions \n Actual \t\t\t Predicted")
target_names=iris.target_names
for j in range(10):
    print(target_names[Ytest[j]],"\t\t\t",target_names[ypred[j]])
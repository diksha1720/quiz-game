from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics


iris=load_iris()
print("target names",iris.target_names)


Xtrain,Xtest,Ytrain,Ytest=train_test_split(iris.data,iris.target)

knn=KNeighborsClassifier(n_neighbors=1)
knn.fit(Xtrain,Ytrain)
ypred=knn.predict(Xtest)

print("Accuarcy :",metrics.accuracy_score(Ytest,ypred))

target_names=iris.target_names
print("First few predictions: \n Actual \t\t\t Predicted\n")
for j in range(10):
    print(target_names[Ytest[j]],"\t\t\t",target_names[ypred[j]])

    
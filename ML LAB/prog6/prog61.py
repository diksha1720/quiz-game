import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

msg=pd.read_csv("naivetrext1.csv",names=["message","labels"])
print("input data and shape")
print(msg.shape)
msg["labelnums"]=msg.labels.map({"pos":1,"neg":0})

X=msg.message
y=msg.labelnums

Xtrain,Xtest,Ytrain,Ytest=train_test_split(X,y)

count_vect=CountVectorizer()
Xtrain_dtm=count_vect.fit_transform(Xtrain)
Xtest_dtm=count_vect.transform(Xtest)
print("feature names", count_vect.get_feature_names())
df=pd.DataFrame(Xtrain_dtm.toarray(),columns=count_vect.get_feature_names())
print(df)
#print(Xtrain)

clf=MultinomialNB()
clf.fit(Xtrain_dtm,Ytrain)
ypred=clf.predict(Xtest_dtm)

print("Accuracy score ", metrics.accuracy_score(Ytest,ypred))
print("Precision :",metrics.precision_score(Ytest,ypred))
print("Recall  :",metrics.recall_score(Ytest,ypred))
print("Confusion matrix  :", metrics.confusion_matrix(Ytest,ypred))

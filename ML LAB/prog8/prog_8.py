import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from sklearn.mixture import GaussianMixture
import matplotlib.pyplot as plt

data=pd.read_csv("ex.csv")
f1=data["V1"].values
f2=data["V2"].values

X=np.array(list(zip(f1,f2)))

plt.title("graph for input data")
plt.scatter(f1,f2,c="black",s=50)
plt.show()

km=KMeans(2,random_state=0)
labels=km.fit(X).predict(X)
print("labels for KMeans ",labels)
centroids=km.cluster_centers_
plt.title("graph for KMeans algo")
plt.scatter(X[:,0],X[:,1],c=labels,s=50)
plt.scatter(centroids[:,0],centroids[:,1],c='blue',marker="*",s=70)
plt.show()

gmm=GaussianMixture(n_components=2)
labels=gmm.fit(X).predict(X)
print("labels for EM algo ",labels)
plt.title("graph for EM algo")
plt.scatter(X[:,0],X[:,1],c=labels,s=50)
plt.show()
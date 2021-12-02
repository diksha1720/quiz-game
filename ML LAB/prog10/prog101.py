import pandas as pd
from numpy import *


def kernel(point,xmat,k):
    m,n=shape(xmat)
    weights=mat(eye(m))
    for j in range(m):
        diff=point-X[j]
        weights[j,j]=diff*diff.T/(-2.0*k**2)
    return weights


def localWeight(point,xmat,ymat,k):
    wei=kernel(point,xmat,k)
    W=(X.T * (wei*X)).I* (X.T* (wei*ymat.T))
    return W



def localWeightRegression(xmat,ymat,k):
    m,n=shape(xmat)
    ypred=zeros(m)
    for j in range(m):
        ypred[j]=xmat[j]*localWeight(xmat[j],xmat,ymat,k)
    return ypred


data=pd.read_csv("tips.csv")
tip=data.tip
bill=data.total_bill
mtip=mat(tip)
mbill=mat(bill)

m=shape(mbill)[1]

one=mat(ones(m))

X=hstack((one.T,mbill.T))
y=mtip

ypred=localWeightRegression(X,y,10)

SortIndex=X[:,1].argsort(0)
xsort=X[SortIndex][:,0]

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(bill,tip,c="green",s=50)
ax.plot(xsort[:,1],ypred[SortIndex],c="red",linewidth=5)
plt.xlabel("total bill")
plt.ylabel("tips")
plt.show()
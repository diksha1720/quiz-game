from numpy import *
import pandas as pd
import matplotlib.pyplot as plt


def kernel(point,xmat,k):
    m,n=shape(xmat)
    weights=mat(eye(m))
    for j in range(m):
        diff=point-X[j]
        weights[j,j]=diff*diff.T/(-2.0*k**2)
    return weights



def localweight(point,xmat,ymat,k):
    wei=kernel(point,xmat,k)
    W=(X.T*(wei*X)).I *(X.T*(wei*ymat.T))
    return W



def localweightregression(xmat,ymat,k):
    m,n=shape(xmat)
    ypred=zeros(m)
    for j in range(m):
        ypred[j]=xmat[j]*localweight(xmat[j],xmat,ymat,k)
    return ypred


data=pd.read_csv("tips.csv")
tips=data.tip
bill=data.total_bill
mtip=mat(tips)
mbill=mat(bill)


m=shape(mbill)[1]

one=mat(ones(m))

X=hstack((one.T,mbill.T))
y=mtip

ypred=localweightregression(X,y,10)

SortIndex=X[:,1].argsort(0)
xsort=X[SortIndex][:,0]

fig=plt.figure()
ax=fig.add_subplot(1,1,1)
ax.scatter(bill,tips,c="red",s=30)
ax.plot(xsort[:,1],ypred[SortIndex],c="green",linewidth=2)
plt.xlabel("total bill")
plt.ylabel("tips")
plt.show()
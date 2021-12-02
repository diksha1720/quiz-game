import numpy as np
import pandas as pd

mush=pd.read_csv("mushroom.csv")
mush.replace('?',np.nan)
print(len(mush.columns)," columns initially. After dropping NA ",len(mush.dropna(axis=1).columns), " remaining ")

mush.dropna(axis=1,inplace=True)

target="class"
features=mush.columns[mush.columns!=target]
classes=mush[target].unique()
test=mush.sample(frac=0.3)
mush=mush.drop(test.index)

probs={}
probcl={}

for x in classes:
    mushcl=mush[mush[target]==x][features]
    clsp={}
    tot=len(mushcl.columns)
    for col in mushcl.columns:
        colp={}
        for val,cnt in mushcl[col].value_counts().iteritems():
            pr=cnt/tot
            colp[val]=pr
            clsp[col]=colp
    probs[x]=clsp
    probcl[x]=len(mushcl)/len(mush)
    
def probabs(x):
    if not isinstance(x,pd.Series):
        raise IOError("arg must be of type series")
    probab={}
    for cl in classes:
        pr=probcl[cl]
        for col,val in x.iteritems():
            try:
                pr*=probs[cl][col][val]
            except:
                pr=0
        probab[cl]=pr
    return probab

def classify(x):
    probab=probabs(x)
    mx=0
    mxcl=""
    for cl,pr in probab.items():
        if pr>mx:
            mx=pr
            mxcl=cl
    return mxcl

b=[]
for i in mush.index:
    b.append(classify(mush.loc[i,features])==mush.loc[i,target])
print("Training dataset")
print(sum(b) ," correct out of ",len(mush))
print("Accuracy ",sum(b)/len(mush))



b=[]
for i in test.index:
    b.append(classify(test.loc[i,features])==test.loc[i,target])
print("Test dataset")
print(sum(b) ," correct out of ",len(test))
print("Accuracy ",sum(b)/len(test))



























        
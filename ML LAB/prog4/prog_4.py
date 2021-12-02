import numpy as np

X=np.array(([2,3],[3,3],[1,9]))
y=np.array(([89],[92],[93]))

y=y/100
X=X/np.amax(X,axis=0)


def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative_sigmoid(x):
    return x*(1-x)

inputlayer=2
hiddenlayer=3
outputlayer=1

wh=np.random.uniform(size=(inputlayer,hiddenlayer))
bh=np.random.uniform(size=(1,hiddenlayer))
wout=np.random.uniform(size=(hiddenlayer,outputlayer))
bout=np.random.uniform(size=(1,outputlayer))

lr=0.1
epoch=10000

for i in range(epoch):
    hinp1=np.dot(X,wh)
    hinp=hinp1+bh
    hlayer_act=sigmoid(hinp)
    
    outinp1=np.dot(hlayer_act.T,wout)
    outinp=outinp1+bout
    output=sigmoid(outinp)
    
    EO=y-output
    outgrad=derivative_sigmoid(output)
    d_output=EO*outgrad
    
    EH=d_output.dot(wout.T)
    hiddengrad=derivative_sigmoid(hlayer_act)
    d_hidden=EH*hiddengrad
    
    wout+=hlayer_act.T.dot(d_output)*lr
    wh+=X.T.dot(d_hidden)*lr
    
print("Input " , X)
print("Actual Output ",y)
print("output ",output)
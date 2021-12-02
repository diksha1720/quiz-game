import numpy as np


X=np.array(([2,3],[3,4],[1,9]))
y=np.array(([89],[82],[92]))

y=y/100
X=X/np.amax(X,axis=0)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative_sigmoid(x):
    return x*(1-x)

inputlayer_neuron=2
hiddenlayer_neuron=3
outputlayer_neuron=1

wh=np.random.uniform(size=(inputlayer_neuron,hiddenlayer_neuron))
bh=np.random.uniform(size=(1,hiddenlayer_neuron))
wout=np.random.uniform(size=(hiddenlayer_neuron,outputlayer_neuron))
bout=np.random.uniform(size=(1,outputlayer_neuron))

epoch=7000
lr=0.1

for i in range(epoch):
    hinp1=X.dot(wh)
    hinp=hinp1+bh
    hlayer_act=sigmoid(hinp)
    
    outinp1=hlayer_act.dot(wout)
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
    
print("X  ",X)
print("Y   ",y)
print("output   ",output)
    
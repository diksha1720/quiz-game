# import numpy as np

# X = np.array(([2, 9], [1, 5], [3, 6]))  # Hours Studied, Hours Slept
# y = np.array(([92], [86], [89]))  # Test Score

# y = y / 100  # max test score is 100
# X = X/np.amax(X,axis=0) # maximum of X array longitudinally

# # Sigmoid Function
# def sigmoid(x):  # this function maps any value between 0 and 1
#     return 1 / (1 + np.exp(-x))


# # Derivative of Sigmoid Function
# def derivatives_sigmoid(x):
#     return x * (1 - x)


# # Variable initialization
# epoch = 10000  # Setting training iterations
# lr = 0.1  # Setting learning rate
# inputlayer_neurons = 2  # number of features in data set
# hiddenlayer_neurons = 3  # number of hidden layers neurons
# output_neurons = 1  # number of neurons of output layer

# # weight and bias initialization
# weight_hidden = np.random.uniform(size=(inputlayer_neurons, hiddenlayer_neurons))
# # bias matrix to the hidden layer
# bias_hidden = np.random.uniform(size=(1, hiddenlayer_neurons))
# # weight matrix to the output layer
# weight_output = np.random.uniform(size=(hiddenlayer_neurons, output_neurons))
# # matrix to the output layer
# bias_output = np.random.uniform(size=(1, output_neurons))

# for i in range(epoch):
#     # Forward Propogation
#     hinp1 = np.dot(X, weight_hidden)
#     hinp = hinp1 + bias_hidden  # bias_hidden GRADIENT Descent
#     hlayer_activation = sigmoid(hinp)

#     outinp1 = np.dot(hlayer_activation, weight_output)
#     outinp = outinp1 + bias_output
#     output = sigmoid(outinp)

#     # Backpropagation
#     # Compare prediction with actual output and calculate the gradient of error
#     # (Actual – Predicted)
#     EO = y - output
#     # Compute the slope/gradient of hidden and output layer neurons
#     outgrad = derivatives_sigmoid(output)

#     # Compute change factor(delta) at output layer, dependent on the gradient
#     # of error multiplied by the slope of output layer activation
#     d_output = EO * outgrad

#     # At this step, the error will propagate back into the network which
#     # means error at hidden layer. we will take the dot product of output
#     # layer delta with weight parameters of edges between the hidden and
#     # output layer (weight_hidden.T).
#     EH = d_output.dot(weight_output.T)

#     # how much hidden layer weight contributed to error
#     hiddengrad = derivatives_sigmoid(hlayer_activation)
#     d_hiddenlayer = EH * hiddengrad

#     # update the weights
#     # dot product of nextlayererror and currentlayerop
#     weight_output += hlayer_activation.T.dot(d_output) * lr
#     bias_output += np.sum(d_output, axis=0, keepdims=True) * lr

#     weight_hidden += X.T.dot(d_hiddenlayer) * lr
#     bias_hidden += np.sum(d_hiddenlayer, axis=0, keepdims=True) * lr


# print("Input:\n" + str(X))
# print("Actual Output:\n" + str(y))
# print("Predicted Output:\n", output)


import numpy as np

X=np.array(([2,9], [3,5], [1,4]))
y=np.array(([89],[80],[87]))

y=y/100
X=X/np.amax(X,axis=0)

def sigmoid(x):
    return 1/(1+np.exp(-x))

def derivative_sigmoid(x):
    return x*(1-x)

inputlayer_neurons=2
hiddenlayer_neurons=3
outputlayer_neurons=1

wh=np.random.uniform(size=(inputlayer_neurons,hiddenlayer_neurons))
bh=np.random.uniform(size=(1,hiddenlayer_neurons))
wout=np.random.uniform(size=(hiddenlayer_neurons,outputlayer_neurons))
bout=np.random.uniform(size=(1,outputlayer_neurons))


epoch=10000
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
    d_hiddenlayer=EH*hiddengrad

    wout+=hlayer_act.T.dot(d_output)*lr
    wh+=X.T.dot(d_hiddenlayer)*lr

print("X ",X)
print("y ",y)
print("output: ",output)

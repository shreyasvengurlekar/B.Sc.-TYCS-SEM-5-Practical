# Back Propagation 
Inputs      Output
0  0  1       0
1  1  1       1 
1  0  1       1
0  1  1       0
# A sigmoid function maps any value to a value between 0 and 1.
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
#sigmoid function
def nlinear(x,deriv=False):
    if(deriv==True):
        return x*(1-x)
    return 1/(1+np.exp(-x))

#input dataset
x=np.array([[0,0,1],
           [1,1,1],
           [1,0,1],
           [0,1,1]])
#print(x)
#output dataset
y=np.array([[0,1,1,0]]).T
#print(y)

#seed random numbers for random distributions
np.random.seed(1)

#initialize weights randomly with mmean 0
synapse0=2*np.random.random((3,1))-1
print(synapse0)



for i in range(1000):
    #forward Propagation
    layer0=x
    layer1=nlinear(np.dot(layer0,synapse0))
    
    layer1_error=y-layer1
    
    #multiply how much error backpropagated
    #slope of the sigmoid at the values in layer1
    layer1_delta=layer1_error*nlinear(layer1,True)
    
    #update error as per the error backpropagates
    synapse0 += np.dot(layer0.T,layer1_delta)
    
print("output after training:")
print(layer1)
print("actual output:")
print(y)
df=[y,layer1]
df
plt.plot(y,layer1)






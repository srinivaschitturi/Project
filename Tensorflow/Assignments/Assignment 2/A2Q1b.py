# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 16:49:49 2018

@author: srini
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

###### Declaring Variables #######

x0=np.zeros([100,1])
x1=np.zeros([100,1])
x2=np.full([100,1],1)
y=np.zeros([100,1])
yact=np.zeros(100)
ypred=np.zeros(100)
cost=0
gradient=0
iteration=0
params=np.random.random(2)*1
#params=np.array([2,1])
weights=np.array([params[0],params[1],-1])
weightsPred=np.array([1,1,1])
weightsPredPrev=2*weightsPred

###### Generating uniformly distributed points in a circle of radius 3 ######

for i in range(100):
    r=np.sqrt(np.random.random())*2 ### Sqrt is used for uniform distribution
    theta=(np.random.random()*2-1)*np.pi
    x1[i]=r*np.cos(theta)
    y[i]=r*np.sin(theta)
    ells = Ellipse(xy=[0,0], width=2/np.sqrt(params[1]), height=2/np.sqrt(params[0]), angle=0,fc='none',ec='b')
    fig = plt.gcf()
    ax = fig.gca()
    ax.add_artist(ells)
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
#plt.plot([-1,1],[slope*(-1),slope*(1)])
x=np.column_stack((np.square(y),np.square(x1),np.square(x2)))

###### Classifying Data ######

for i in range(100):
    if (np.dot(x[i],weights))>0:
        yact[i]=1
        plt.scatter(x1[i],y[i],c='g')
    else:
        yact[i]=0
        plt.scatter(x1[i],y[i],c='r')
    ypred[i]=1/(1+np.power(np.e,-np.dot(x[i],weightsPred)))
    
###### Split data into Test Train ######
j=0.7
yactTrain=yact[0:int(len(x)*j)]
ypredTrain=ypred[0:int(len(x)*j)]
xtrain=x[0:int(len(x)*j)]
yactTest=yact[int(len(x)*j)+1:len(x)]
ypredTest=ypred[int(len(x)*j)+1:len(x)]
xtest=x[int(len(x)*j)+1:len(x)]
    
###### Gradient Descent - Training data ######

while np.linalg.norm(weightsPred-weightsPredPrev)>0.00001:
    for i in range(70):        
        #cost-=(yact*np.log10(ypred)+(1-yact)*np.log10(1-ypred))
        gradient=np.dot((yactTrain[i]-ypredTrain[i]),xtrain[i])
        weightsPredPrev=weightsPred
        weightsPred=weightsPred+gradient*1E-2 
        #print(weightsPred)
        ypredTrain[i]=1/(1+np.power(np.e,-np.dot(xtrain[i],weightsPred)))
    #rmse=np.linalg.norm(cost)
    iteration=iteration+1
    #plt.scatter(iteration,rmse)
    #if j==0.7:
print(weightsPred)
    
###### Testing Data ######

for i in range(int((1-j)*int(len(x)))-1):
    ypredTest[i]=1/(1+np.power(np.e,-np.dot(xtest[i],weightsPred)))
    cost-=(yactTest[i]*np.log10(ypredTest[i])+(1-yactTest[i])*np.log10(1-ypredTest[i]))
    if ypredTest[i]<0.5:
        ypredTest[i]=0
    else:
        ypredTest[i]=1
print(cost)
print(np.mean(ypredTest==yactTest))
ells1 = Ellipse(xy=[0,0], width=2*np.sqrt(-weightsPred[2]/weightsPred[1]), height=2*np.sqrt(-weightsPred[2]/weightsPred[0]), angle=0,fc='none',ec='r')
ax.add_artist(ells1)
#plt.plot([-1,1],[-weightsPred[1]*(-1)/weightsPred[0],-weightsPred[1]*(1)/weightsPred[0]])
plt.show()
"""
input1=input("Enter x coordinate")
input2=input("Enter y coordinate")
if 1/(1+np.power(np.e,-np.dot([float(input2),float(input1),1],weightsPred)))>=0.5:
    print("TRUE")
else:
    print("FALSE")
    """
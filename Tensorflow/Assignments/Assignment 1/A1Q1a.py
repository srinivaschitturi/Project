# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 01:10:58 2018

@author: srini
"""
def grad(noise):
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot
    x1=np.full(31,1)
    x0=np.full(31,1)
    for i in range(31):
        x1[i]=i
    y=np.square(x1)+5*x1
    y=np.matrix(y)
    x=np.matrix([x1,x0])
    if noise==1:
        stddeviation=y.std(0)
    print(y)
    weights=np.matrix([-1.0,-1.0])
    weightsprev=weights*2
    matplotlib.pyplot.scatter(np.array(x[0,:]),np.array(y[0,:]))
    while np.linalg.norm(weights-weightsprev)>0.0001:
        error=y.transpose()-np.dot(x.transpose(),weights.transpose())
        cost=np.dot(error.transpose(),x.transpose())
        weightsprev=weights
        """increment=np.dot(learnRate,cost.transpose())"""
        weights=weights+cost*0.0001
        print(weights)
    matplotlib.pyplot.plot([0,30],[-144.87701253,904.941375])
    matplotlib.pyplot.show()
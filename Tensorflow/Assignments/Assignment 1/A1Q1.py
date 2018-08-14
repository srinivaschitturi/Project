def batchGD():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot
    data = pd.read_csv("C:\\Users\\srini\\OneDrive\\Academics\\ML courses\\ID 5030\\Assignments\\Assignment 1\\assignment1.csv")
    """print(data)"""
    data=data.dropna()
    print(data.iloc[3,3])
    weights=np.array([-1,0])
    size=len(data.index())
    duplicate=np.full(size,1)
    x=np.array([data.iloc[:,3],duplicate])
    y=data.iloc[:,1]
    learnRate=1
    matplotlib.pyplot.scatter(data.iloc[:,3],data.iloc[:,1])
    matplotlib.pyplot.show()
        
    """"print(data.count)"""
    for j in range(1,100):   
        error=y-np.dot(weights,x)
        cost=np.dot(error.transpose(),x)
        increment=cost*learnRate
        w=w+increment
    print(w)
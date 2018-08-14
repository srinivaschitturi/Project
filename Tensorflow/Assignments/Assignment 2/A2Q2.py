import gzip
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

aTrain=np.zeros(1,dtype=int)
aTest=np.zeros(1,dtype=int)
countTrain=0;
countTest=0;
weightsPred=np.full(785,1)
weightsPredPrev=weightsPred*2

image1=np.zeros([28,28])
iteration=0       
cost=0

with gzip.open('C:\\Users\\srini\\OneDrive\\Academics\\ML courses\\ID 5030\\Assignments\\Assignment 2\\Digits\\train-images-idx3-ubyte.gz', 'rb') as f:
            imgarrayTrain = np.frombuffer(f.read(),dtype=np.uint8, offset=16)

with gzip.open('C:\\Users\\srini\\OneDrive\\Academics\\ML courses\\ID 5030\\Assignments\\Assignment 2\\Digits\\train-labels-idx1-ubyte.gz', 'rb') as f:
            labelsTrain = np.frombuffer(f.read(),dtype=np.uint8, offset=8)
            
with gzip.open('C:\\Users\\srini\\OneDrive\\Academics\\ML courses\\ID 5030\\Assignments\\Assignment 2\\Digits\\t10k-images-idx3-ubyte.gz', 'rb') as f:
            imgarrayTest = np.frombuffer(f.read(),dtype=np.uint8, offset=16)

with gzip.open('C:\\Users\\srini\\OneDrive\\Academics\\ML courses\\ID 5030\\Assignments\\Assignment 2\\Digits\\t10k-labels-idx1-ubyte.gz', 'rb') as f:
            labelsTest = np.frombuffer(f.read(),dtype=np.uint8, offset=8)
            
            
for k in range(len(labelsTrain)):
    if (labelsTrain[k]==1) | (labelsTrain[k]==0):
        countTrain=countTrain+1
        if countTrain==1:
            aTrain[0]=k
        else:
            aTrain=np.concatenate([aTrain,[int(k)]])

for k in range(len(labelsTest)):
    if (labelsTest[k]==1) | (labelsTest[k]==0):
        countTest=countTest+1
        if countTest==1:
            aTest[0]=k
        else:
            aTest=np.concatenate([aTest,[int(k)]])
            
xTrain=np.zeros([len(aTrain),785])
xTrain[:,784]=np.full(len(aTrain),1)

xTest=np.zeros([len(aTest),785])
xTest[:,784]=np.full(len(aTest),1)

yactTrain=np.zeros([len(aTrain)])
ypredTrain=np.zeros([len(aTrain)])

yactTest=np.zeros([len(aTest)])
ypredTest=np.zeros([len(aTest)])

for i in range(len(aTrain)):
    xTrain[i,0:784]=imgarrayTrain[784*aTrain[i]:784*(aTrain[i]+1)]
    if labelsTrain[aTrain[i]]==0:
        yactTrain[i]=0
    else:
        yactTrain[i]=1
    ypredTrain[i]=1/(1+np.power(np.e,-np.dot(xTrain[i],weightsPred)))
 
for i in range(len(aTest)):
    xTest[i,0:784]=imgarrayTest[784*aTest[i]:784*(aTest[i]+1)]
    if labelsTest[aTest[i]]==0:
        yactTest[i]=0
    else:
        yactTest[i]=1

for i in range(28):
    for j in range(28):
            image1[i][j]=xTrain[6,28*(i)+j]
plt.imshow(image1, cmap='gray', vmin=0, vmax=255)
plt.show()

for i in range(100):
    for l in range(len(aTrain)):        
        gradient=np.dot((yactTrain[l]-ypredTrain[l]),xTrain[l,:])
        weightsPredPrev=weightsPred
        weightsPred=weightsPred+gradient*1E-5
        ypredTrain[l]=1/(1+np.power(np.e,-np.dot(xTrain[l],weightsPred)))
    iteration=iteration+1

for i in range(len(aTest)):
    ypredTest[i]=1/(1+np.power(np.e,-np.dot(xTest[i],weightsPred)))
    cost-=(yactTest[i]*np.log10(ypredTest[i])+(1-yactTest[i])*np.log10(1-ypredTest[i]))
    if ypredTest[i]<0.5:
        ypredTest[i]=0
    else:
        ypredTest[i]=1
print(cost)
print(np.mean(ypredTest==yactTest))
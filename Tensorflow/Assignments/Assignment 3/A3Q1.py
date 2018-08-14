import numpy as np
import tensorflow as tf
import pandas as pd

path="C:\\Users\\srini\\OneDrive\\Academics\\ML courses\\ID 5030\\Assignments\\Assignment 3\\30_train_features.csv"
data=pd.read_csv(path)
pathTest="C:\\Users\\srini\\OneDrive\\Academics\\ML courses\\ID 5030\\Assignments\\Assignment 3\\30_test_features.csv"
dataTest=pd.read_csv(pathTest)
XData=data.iloc[:,0:30].values
XDataTest=dataTest.iloc[:,0:30].values
for i in range(30):
    XData[:,i]=(XData[:,i]-np.mean(XData[:,i]))/(np.std(XData[:,i]))
    XDataTest[:,i]=(XDataTest[:,i]-np.mean(XDataTest[:,i]))/(np.std(XDataTest[:,i]))
bias=tf.Variable(tf.zeros(3,dtype=tf.float64))
extra=np.zeros([98,1])
extraTest=np.zeros([33,1])
YData=np.column_stack((np.transpose(np.matrix(np.float64(data.iloc[:,30].values))),extra,extra))
YDataTest=np.column_stack((np.transpose(np.matrix(np.float64(dataTest.iloc[:,30].values))),extraTest,extraTest))
for i in range(98):
    if YData[i,0]>=450:
        YData[i,0]=1
        YData[i,1]=0
        YData[i,2]=0
    elif (YData[i,0]>=300) & (YData[i,0]<450):
        YData[i,0]=0
        YData[i,1]=1
        YData[i,2]=0
    else:
        YData[i,0]=0
        YData[i,1]=0
        YData[i,2]=1

for i in range(len(YDataTest)):   
    if YDataTest[i,0]>=450:
        YDataTest[i,0]=1
        YDataTest[i,1]=0
        YDataTest[i,2]=0
    elif (YDataTest[i,0]>=300) & (YDataTest[i,0]<450):
        YDataTest[i,0]=0
        YDataTest[i,1]=1
        YDataTest[i,2]=0
    else:
        YDataTest[i,0]=0
        YDataTest[i,1]=0
        YDataTest[i,2]=1

X=tf.placeholder(tf.float64,shape=(None,30))
Y=tf.placeholder(tf.float64,shape=(None,3))
weights=tf.Variable(tf.ones([30,3],tf.float64))
yPred=tf.nn.softmax(tf.matmul(X,weights)+bias)  
loss=-tf.reduce_sum(Y*tf.log(yPred)+(1-Y)*tf.log(1-yPred))
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        sess.run([optimizer], feed_dict={X:XData, Y:YData})
    correct_prediction = tf.equal(tf.argmax(yPred,1), tf.argmax(Y,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float64))
    print(sess.run(accuracy, feed_dict={X: XDataTest, Y: YDataTest}))
    yPredn=tf.one_hot(tf.argmax(yPred,1),3)

    predn, act= sess.run([yPredn,Y], feed_dict={X: XDataTest, Y: YDataTest})
    sens=0
    count=0
    for i in range(33):
        if (i==14) | (i==24) | (i==32):
            print(sens/count)
            sens=0
            count=0
        if(np.all(predn[i]==act[i])):
            sens+=1
        count+=1
        

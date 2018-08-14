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
bias=tf.Variable(tf.zeros(1,dtype=tf.float64))
YData=np.transpose(np.matrix(np.float64(data.iloc[:,30].values)))
YDataTest=np.transpose(np.matrix(np.float64(dataTest.iloc[:,30].values)))
for i in range(98):
    if YData[i,0]>=300:
        YData[i,0]=1
    else:
        YData[i,0]=0

for i in range(len(YDataTest)):   
    if YDataTest[i,0]>=300:
        YDataTest[i,0]=1
    else:
        YDataTest[i,0]=0
X=tf.placeholder(tf.float64,shape=(None,30))
Y=tf.placeholder(tf.float64,shape=(98,1))
y_ = tf.placeholder(tf.float64, [33,1])
weights=tf.Variable(tf.ones([30,1],tf.float64))
yPred=tf.nn.sigmoid(-(tf.matmul(X,weights)+bias))
loss=-tf.reduce_sum(Y*tf.log(yPred)+(1-Y)*tf.log(1-yPred))
optimizer=tf.train.GradientDescentOptimizer(learning_rate=0.0005).minimize(loss)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(1000):
        sess.run([optimizer], feed_dict={X:XData, Y:YData})
    yPred=tf.cast(tf.greater_equal(yPred,tf.constant(0.5,dtype=tf.float64)),tf.float64)
    correct_prediction = tf.equal(yPred,y_)
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float64))
    print(sess.run(accuracy, feed_dict={X: XDataTest, y_: YDataTest}))
    prod=tf.multiply(yPred,y_)
    summation=yPred+y_
    ab=tf.cast(tf.size(y_),tf.float64)-tf.reduce_sum(y_)
    specificity=tf.reduce_sum(tf.cast(tf.equal(yPred,tf.constant(0.0,tf.float64)),tf.float64))/ab
    truepos=tf.reduce_sum(prod)
    sensitivity=truepos/tf.reduce_sum(y_)
    print(sess.run([sensitivity,specificity], feed_dict={X: XDataTest, y_: YDataTest}))

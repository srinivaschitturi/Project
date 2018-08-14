# -*- coding: utf-8 -*-
"""
Created on Tue Mar 20 21:45:51 2018

@author: srini
"""

import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data as mnist_data
mnist = mnist_data.read_data_sets("data", one_hot=True)

X = tf.placeholder(tf.float32, shape=[None, 28, 28, 1])
Y_ = tf.placeholder(tf.int32, [None, 10])

eval_data=mnist.test.images
eval_data=np.reshape(eval_data,[10000,28,28,1])
eval_labels=mnist.test.labels

Y1 = tf.layers.conv2d(X, filters = 6, kernel_size = [5,5], padding =  "same", activation = tf.nn.relu)
Y1 = tf.layers.max_pooling2d(Y1, pool_size=[2,2], strides=2)
Y2 = tf.layers.conv2d(Y1, filters = 16, kernel_size = [5,5], padding =  "same", activation = tf.nn.relu)
Y2 = tf.layers.max_pooling2d(Y2, pool_size=[2,2], strides=2)


YY = tf.reshape(Y2, shape=[-1, 7 * 7 * 16])

YY2 = tf.layers.dense(YY, 120, activation= tf.nn.relu)

YY3 = tf.layers.dense(YY2, 84, activation= tf.nn.relu)

YY4 = tf.layers.dense(YY3, 10, activation= tf.nn.relu)

cross_entropy = tf.nn.softmax_cross_entropy_with_logits_v2(logits=YY4, labels=Y_)

learning_rate = 0.003
training_epochs = 10
train_step = tf.train.AdamOptimizer(learning_rate).minimize(cross_entropy)

init = tf.global_variables_initializer()
sess = tf.Session()
sess.run(init)

for i in range(550):
    # load batch of images and correct answers
    batch = mnist.train.next_batch(100)
    batch_X = batch[0]
    batch_X = np.reshape(batch_X , [100, 28, 28, 1])
    batch_Y = np.asarray(batch[1], dtype = np.int32)
   

    # train
    sess.run(train_step, feed_dict= {X: batch_X, Y_: batch_Y})

sess.run([train_step], feed_dict={X: batch_X, Y_: batch_Y})
correct_prediction = tf.equal(tf.argmax(YY4,1), tf.argmax(Y_,1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
print(sess.run(accuracy, feed_dict={X:eval_data, Y_:eval_labels}))
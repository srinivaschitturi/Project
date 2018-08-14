import tensorflow as tf
import numpy as np
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data", one_hot=True)

val_file = mnist.validation.images
val_labels = mnist.validation.labels
eval_data = mnist.test.images
eval_labels = np.asarray(mnist.test.labels, dtype=np.int32)
input_layer = tf.placeholder(tf.float32,[None,784])
input_labels = tf.placeholder(tf.int32,[None,10])
train_file = tf.reshape(input_layer, [-1, 28, 28, 1])
conv1 = tf.layers.conv2d(inputs=train_file,filters=6,kernel_size=[5, 5],padding="same",activation=tf.nn.relu)
pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[2, 2], strides=2)
conv2 = tf.layers.conv2d(inputs=pool1,filters=16,kernel_size=[5, 5],padding="same",activation=tf.nn.relu)
pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 2], strides=2)
poolflat=tf.reshape(pool2, [-1,7*7*16])
dense1=tf.layers.dense(poolflat,units=120,activation=tf.nn.relu,use_bias=True)
dense2=tf.layers.dense(dense1,units=84,activation=tf.nn.relu,use_bias=True)
dense3=tf.layers.dense(dense2,units=10,activation=tf.nn.relu,use_bias=True)
loss = tf.nn.softmax_cross_entropy_with_logits_v2(labels=input_labels, logits=dense3)
optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001).minimize(loss)
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(440):
        print(i)
        batch=mnist.train.next_batch(125)
        data = batch[0]
        labels = np.asarray(batch[1], dtype=np.int32)
        for j in range(10):
            sess.run(optimizer, feed_dict={input_layer:data, input_labels:labels})
        
    
    correct_prediction = tf.equal(tf.argmax(dense3,1), tf.argmax(input_labels,1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
    print(sess.run(accuracy, feed_dict={input_layer:eval_data, input_labels:eval_labels}))
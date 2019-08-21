#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# 学习tensorflow https://www.tensorflow.org/

"""
Please note, this code is only for python 3+. If you are using python 2+, please modify the code accordingly.
"""
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets('MNIST_data', one_hot=True)


class len_tf:
    # def one(self):
    #
    #     # 创建数据
    #     x_data = np.random.rand(100).astype(np.float32)
    #     y_data = x_data*0.1 + 0.3
    #
    #     # 创建结构
    #     Weights = tf.Variable(tf.random_uniform([1],-1.0,1.0)) # 随机生产一维，-1到1之间
    #     biases = tf.Variable(tf.zeros([1]))
    #
    #     y = Weights*x_data + biases
    #
    #     loss = tf.reduce_mean(tf.square(y-y_data)) # 误差
    #     optimizer = tf.train.GradientDescentOptimizer(0.5)# 优化器 0.5是小于1的数，是学习效率
    #     train = optimizer.minimize(loss)# 用优化器减少误差
    #
    #     init = tf.global_variables_initializer()  # 初始化
    #
    #     # 初始化开始
    #     sess = tf.Session()
    #     sess.run(init) # 激活
    #
    #     for step in range(201):
    #         sess.run(train) # 开始训练
    #         if step %20 == 0:
    #             print(step,sess.run(Weights),sess.run(biases))
    #
    # def two(self):
    #     matrix1 = tf.constant([[3, 3]])
    #     matrix2 = tf.constant([[2],
    #                            [2]])
    #     product = tf.matmul(matrix1, matrix2)
    #
    #     # 方法1
    #     # sess = tf.Session()
    #     # result = sess.run(product)
    #     # print(result)
    #     # sess.close()
    #
    #     # 方法2
    #     with tf.Session() as sess:
    #         result2 = sess.run(product)
    #         print(result2)
    # def three(self):
    #     state = tf.Variable(0,name='counter') # 定义变量，0和名字
    #     # print(state.name)
    #
    #     one = tf.constant(1)
    #     new_value = tf.add(state , one)
    #     update = tf.assign(state,new_value)
    #
    #     init = tf.global_variables_initializer() # 有定义变量一定要有这一句
    #     with tf.Session() as sess:
    #         sess.run(init) # 有定义变量一定要初始化，否则变量无效
    #         for _ in range(3):
    #             sess.run(update)
    #             # print(sess.run(state))
    #
    # def four(self):
    #     input1 = tf.placeholder(tf.float32)
    #     input2 = tf.placeholder(tf.float32)
    #
    #     output = tf.multiply(input1,input2)
    #
    #     with tf.Session() as a:
    #         d = a.run(output,feed_dict={input1:7,input2:2})
    #         print(d)

    #构造添加一个神经层的函数。
    def add_layer(inputs, in_size, out_size,n_layer, activation_function=None):
        layer_name = 'layer%s'%n_layer
        with tf.name_scope('layer'):
            with tf.name_scope('weigts'):
                Weights = tf.Variable(tf.random_normal([in_size,out_size]),name='W')
                tf.summary.histogram(layer_name+'/weights',Weights)

            with tf.name_scope('biases'):
                biases = tf.Variable(tf.zeros([1,out_size]) + 0.1,name='b')
                tf.summary.histogram(layer_name+'/biases',biases)

            with tf.name_scope('Wx_plus_b'):
                Wx_plus_b = tf.matmul(inputs,Weights) + biases

            if activation_function is None:
                outputs = Wx_plus_b
            else:
                outputs = activation_function(Wx_plus_b)
            tf.summary.histogram(layer_name + '/outputs', outputs)
            return outputs
    #导入数据
    x_data = np.linspace(-1, 1, 300, dtype=np.float32)[:, np.newaxis]
    noise = np.random.normal(0, 0.05, x_data.shape).astype(np.float32)
    y_data = np.square(x_data) - 0.5 + noise
    #利用占位符定义我们所需的神经网络的输入
    with tf.name_scope('inputs'):
        xs = tf.placeholder(tf.float32,[None,784],name='x_input')
        ys = tf.placeholder(tf.float32,[None,10],name='y_input')

    #搭建网络
    l1 = add_layer(xs,1,10,n_layer=1,activation_function=tf.nn.relu)
    prediction = add_layer(l1, 10, 1, n_layer=2,activation_function=None)

    with tf.name_scope('loss'):
        loss = tf.reduce_mean(tf.reduce_sum(tf.square(ys - prediction),
                                        reduction_indices=[1]))
        tf.summary.scalar('loss',loss)
    with tf.name_scope('train'):
        train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

    init = tf.global_variables_initializer()
    sess = tf.Session()
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter("data/", sess.graph)
    # tensorboard --logdir=data --host=localhost --port=8088 命令运行
    sess.run(init)


    fig = plt.figure()#生产图片框
    ax = fig.add_subplot(1,1,1)#连续画图
    ax.scatter(x_data,y_data)#用点的形式
    plt.ion()


    for i in range(1000):
        sess.run(train_step,feed_dict={xs:x_data,ys:y_data})
        if i % 50 ==0:
            rs = sess.run(merged,feed_dict={xs:x_data,ys:y_data})
            writer.add_summary(rs,i)
            # print(sess.run(loss,feed_dict={xs:x_data,ys:y_data}))
            # try:
            #     ax.lines.remove(lines[0])
            #
            # except Exception:
            #     pass
            #
            # prediction_value = sess.run(prediction,feed_dict={xs:x_data})
            # lines = ax.plot(x_data,prediction_value,'r-',lw=5)
            # plt.pause(0.1)


    #如果在脚本中使用ion()命令开启了交互模式，没有使用ioff()关闭的话，则图像会一闪而过，并不会常留。
    # 要想防止这种情况，需要在plt.show()之前加上ioff()命令。
    plt.ioff()
    plt.show()


len_tf()

from datamanager.data import Data
from pprint import pprint
import tensorflow as tf
import numpy as np
import math

class TensorFlower:
	def __init__(self, start, end):
		
		self.data = Data(start, end)
	
	def trainShow(self):
		return
		
	def trainWin(self):
		#test data
		xData = np.array([
			[0., 0., 0.],
			[0., 0., 1.],
			[0., 1., 0.],
			[0., 1., 1.],
			[1., 0., 0.],
			[1., 0., 1.],
			[1., 1., 0.],
			[1., 1., 1.]])
		yData = np.array([
			[1., 0., 0., 0.],
			[0., 1., 0., 0.],
			[0., 1., 0., 0.],
			[0., 0., 1., 0.],
			[0., 1., 0., 0.],
			[0., 0., 1., 0.],
			[0., 0., 1., 0.],
			[0., 0., 0., 1.]])
		xCount = 3
		yCount = 4
		
		#real data
		#xData = self.getInputs(start,end)
		#yData = self.getWinOutputs(start,end)
		xCount = self.data.MAX_TEAMS * self.data.INPUTS_PER_TEAMS
		yCount = self.data.MAX_TEAMS
		HIDDEN_NODES = 128 
		factor = 0.05
		batchSize = 256
		
		# input
		x = tf.placeholder(tf.float32, [None, xCount])
		
		# hidden 1
		w1 = self.getWeights(xCount, HIDDEN_NODES)
		b1 = self.getBiases(HIDDEN_NODES)
		h1 = tf.nn.relu(tf.matmul(x, w1) + b1)
		
		# hidden 2
		w2 = self.getWeights(HIDDEN_NODES, HIDDEN_NODES)
		b2 = self.getBiases(HIDDEN_NODES)
		h2 = tf.nn.relu(tf.matmul(h1, w2) + b2)
		
		# hidden 3
		w3 = self.getWeights(HIDDEN_NODES, HIDDEN_NODES)
		b3 = self.getBiases(HIDDEN_NODES)
		hN = tf.nn.relu(tf.matmul(h2, w3) + b3)
		
		# output
		W_logits = tf.Variable(tf.truncated_normal([HIDDEN_NODES, yCount] , stddev=0.1))
		b_logits = tf.Variable(tf.zeros([yCount]))
		logits = tf.matmul(hN, W_logits) + b_logits
		y = tf.nn.softmax(logits)
		
		# clean prediction
		#ones = tf.ones([raceCount], tf.int64)
		#prediction = tf.add(tf.argmax(y,1), ones)
		
		# wanted output
		yWanted = tf.placeholder(tf.float32, [None, yCount])

		# error
		cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits, yWanted)
		loss = tf.reduce_mean(cross_entropy)

		# training
		train_op = tf.train.GradientDescentOptimizer(factor).minimize(loss)
		
		# eval
		correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(yWanted,1))
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))

		# init
		init_op = tf.initialize_all_variables()
		sess = tf.Session()
		sess.run(init_op)
		
		# train
		for i in range(100000):
			xBatch, yBatch = self.data.nextBacthWin(batchSize)
			_, loss_val = sess.run([train_op, loss], feed_dict={x: xBatch, yWanted: yBatch})
			if i % 100 == 0:
				accuracyValueTrain = sess.run(accuracy, feed_dict={x: self.data.training['input'], yWanted: self.data.training['win']})
				accuracyValueTest = sess.run(accuracy, feed_dict={x: self.data.test['input'], yWanted: self.data.test['win']})
				print("Step:", i, 
					"\tLoss:", loss_val, 
					"\tTrain:", accuracyValueTrain, 
					"\tTest:", accuracyValueTest)
		
		# print final prediction
		# print (sess.run(prediction, feed_dict={x: self.data.inputs}))
		
		sess.close()
	
	def getWeights(self, i, o):
		return tf.Variable(tf.truncated_normal([i, o], 
				stddev = 1.0 / math.sqrt(float(i))))
	
	def getBiases(self, c):
		return tf.Variable(tf.zeros([c]))
		
		
	
		
	

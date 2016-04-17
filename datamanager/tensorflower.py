from datamanager.conf import Conf
from pprint import pprint
import tensorflow as tf
import numpy as np
import math

class TensorFlower:
	def __init__(self):
		self.MAX_TEAMS = 30
		self.INPUTS_PER_TEAMS = 12
	
	def trainShow(self, start,end):
		return
		
	def trainWin(self, start,end):
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
		xData = self.getInputs(start,end)
		yData = self.getWinOutputs(start,end)
		xCount = 30*12
		yCount = 30
		HIDDEN_NODES = 64 
		factor = 0.2
		raceCount = 1413
		
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
		
		# cleen prediction
		ones = tf.ones([raceCount], tf.int64)
		prediction = tf.add(tf.argmax(y,1), ones)
		
		# wanted output
		yWanted = tf.placeholder(tf.float32, [None, yCount])

		# error
		cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits, yWanted)
		loss = tf.reduce_mean(cross_entropy)

		# training
		train_op = tf.train.GradientDescentOptimizer(factor).minimize(loss)

		# init
		init_op = tf.initialize_all_variables()
		sess = tf.Session()
		sess.run(init_op)
		
		# train
		for i in range(10000):
			_, loss_val = sess.run([train_op, loss], feed_dict={x: xData, yWanted: yData})
			if i % 100 == 0:
				print("Step:", i, "Current loss:", loss_val)
		
		# print final prediction
		print (sess.run(prediction, feed_dict={x: xData}))
		
		sess.close()
	
	def getWeights(self, i, o):
		return tf.Variable(tf.truncated_normal([i, o], 
				stddev = 1.0 / math.sqrt(float(i))))
	
	def getBiases(self, c):
		return tf.Variable(tf.zeros([c]))
		
		
	def getInputs(self, start,end):
		inputs = []
		fname = Conf.TRAINING_SET_INPUTS.replace('START',start).replace('END',end)
		with open(fname, 'r') as f:
			for line in f:
				a = [float(x) for x in line.split(';')]
				while(len(a) < self.MAX_TEAMS*self.INPUTS_PER_TEAMS):
					a.append(0.0)
				inputs.append(a)
		inputs = np.array(inputs)
		return inputs
		
	def getShowOutputs(self, start,end):
		outputs = []
		fname = Conf.TRAINING_SET_SHOWS.replace('START',start).replace('END',end)
		with open(fname, 'r') as f:
			for line in f:
				list = [(int(x) if x!='\n' else 0) for x in line.split(';')]
				a = []
				for i in range(1, self.MAX_TEAMS+1):
					if i in list:
						a.append(1.0)
					else:
						a.append(0.0)
				outputs.append(a)
		outputs = np.array(outputs)
		return outputs
		
	def getWinOutputs(self, start,end):
		outputs = []
		fname = Conf.TRAINING_SET_WINS.replace('START',start).replace('END',end)
		with open(fname, 'r') as f:
			for line in f:
				list = [(int(x) if x!='\n' else 0) for x in line.split(';')]
				a = []
				for i in range(1, self.MAX_TEAMS+1):
					if i in list:
						a.append(1.0)
					else:
						a.append(0.0)
				outputs.append(a)
		outputs = np.array(outputs)
		return outputs

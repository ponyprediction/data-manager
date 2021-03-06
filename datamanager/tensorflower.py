
from datamanager.data import Data
from pprint import pprint
import tensorflow as tf
import numpy as np
import math

class TensorFlower:
	def __init__(self, start, end):
		
		self.data = Data(start, end)
	
	def trainShow(self):
		#real data
		xCount = self.data.MAX_TEAMS * self.data.INPUTS_PER_TEAMS
		yCount = self.data.MAX_TEAMS
		factor = 0.05
		batchSize = 100
		xx = 1.2
		
		print(xCount)
		print(yCount)
		
		# input
		x = tf.placeholder(tf.float32, [None, xCount])
		
		# hidden 1
		h1Count = int((xCount-yCount) * 0.75 * xx + yCount)
		w1 = self.getWeights(xCount, h1Count)
		b1 = self.getBiases(h1Count)
		h1 = tf.nn.relu(tf.matmul(x, w1) + b1)
		
		# hidden 2
		h2Count = int((xCount-yCount) * 0.50 * xx + yCount)
		w2 = self.getWeights(h1Count, h2Count)
		b2 = self.getBiases(h2Count)
		h2 = tf.nn.relu(tf.matmul(h1, w2) + b2)
		
		# hidden 3
		h3Count = int((xCount-yCount) * 0.25 * xx + yCount)
		w3 = self.getWeights(h2Count, h3Count)
		b3 = self.getBiases(h3Count)
		h3 = tf.nn.relu(tf.matmul(h2, w3) + b3)
		
		"""# hidden 4
		w4 = self.getWeights(HIDDEN_NODES, HIDDEN_NODES)
		b4 = self.getBiases(HIDDEN_NODES)
		hN = tf.nn.relu(tf.matmul(h3, w4) + b4)"""
		
		# output
		W_logits = tf.Variable(tf.truncated_normal([h3Count, yCount] , stddev=0.1))
		b_logits = tf.Variable(tf.zeros([yCount]))
		logits = tf.matmul(h3, W_logits) + b_logits
		y = tf.nn.softmax(logits)
		y = logits
		#y = logits
		
		# clean prediction
		#ones = tf.ones([raceCount], tf.int64)
		#prediction = tf.add(tf.argmax(y,1), ones)
		
		# wanted output
		yWanted = tf.placeholder(tf.float32, [None, yCount])

		# error
		#cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits, yWanted)
		#loss = tf.reduce_mean(cross_entropy)
		#loss = 0.1		
		diff = tf.reduce_sum(tf.abs(tf.sub(y, yWanted)))
		sumWanted = tf.reduce_sum(yWanted)
		sum = tf.reduce_sum(y)
		
		loss0 = tf.truediv(sumWanted, sum)
		loss1 = tf.truediv(diff, sumWanted)
		loss2 = tf.mul(loss0, loss1)

		# training
		train_op = tf.train.GradientDescentOptimizer(factor).minimize(loss1)
		
		# eval
		correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(yWanted,1))
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
		
		#stuff

		# init
		init_op = tf.initialize_all_variables()
		sess = tf.Session()
		sess.run(init_op)
		
		# train
		s = 200
		for i in range(10000000):
			xBatch, yBatch = self.data.nextBacthShow(batchSize)
			_, loss_val = sess.run([train_op, loss1], feed_dict={x: xBatch, yWanted: yBatch})
			if i % (s*50) == 0:
				print('Step\t'
					'| Loss 1\t'
					'| Loss 2\t'
					'| Acc\t\t'
					'| Diff\t\t'
					'| Sumw\t\t'
					'| Sum\t\t'
					
					'|| Loss 1\t'
					'| Loss 2\t'
					'| Acc\t\t'
					'| Diff\t\t'
					'| Sumw\t\t'
					'| Sum\t\t')
			if i % s == 0:
				accuracyValueTrain = sess.run(accuracy, feed_dict={x: self.data.training['input'], yWanted: self.data.training['show']})
				diffTrain = sess.run(diff, feed_dict={x: self.data.training['input'], yWanted: self.data.training['show']})
				loss1Train = sess.run(loss1, feed_dict={x: self.data.training['input'], yWanted: self.data.training['show']})
				loss2Train = sess.run(loss2, feed_dict={x: self.data.training['input'], yWanted: self.data.training['show']})
				sumWantedTrain = sess.run(sumWanted, feed_dict={x: self.data.training['input'], yWanted: self.data.training['show']})
				sumTrain = sess.run(sum, feed_dict={x: self.data.training['input'], yWanted: self.data.training['show']})
				
				accuracyValueTest = sess.run(accuracy, feed_dict={x: self.data.test['input'], yWanted: self.data.test['show']})
				diffTest = sess.run(diff, feed_dict={x: self.data.test['input'], yWanted: self.data.test['show']})
				loss1Test = sess.run(loss1, feed_dict={x: self.data.test['input'], yWanted: self.data.test['show']})
				loss2Test = sess.run(loss2, feed_dict={x: self.data.test['input'], yWanted: self.data.test['show']})
				sumWantedTest = sess.run(sumWanted, feed_dict={x: self.data.test['input'], yWanted: self.data.test['show']})
				sumTest = sess.run(sum, feed_dict={x: self.data.test['input'], yWanted: self.data.test['show']})
				
				print("%7d\t|" % i, 
					"\t%4.4f\t|" % loss1Train,
					"\t%4.2f\t|" % loss2Train,
					"\t%4.4f\t|" % accuracyValueTrain, 
					"\t%4.2f\t|" % diffTrain,
					"\t%4.2f\t|" % sumWantedTrain,
					"\t%4.2f\t||" % sumTrain,
					
					"\t%4.4f\t|" % loss1Test,
					"\t%4.2f\t|" % loss2Test,
					"\t%4.4f\t|" % accuracyValueTest, 
					"\t%4.2f\t|" % diffTest,
					"\t%4.2f\t|" % sumWantedTest,
					"\t%4.2f\t|" % sumTest,
					)
		sess.close()
		
	def trainWin(self):
		#real data
		xCount = self.data.MAX_TEAMS * self.data.INPUTS_PER_TEAMS
		yCount = self.data.MAX_TEAMS
		factor = 0.05
		batchSize = 100
		xx = 1.2
		
		print(xCount)
		print(yCount)
		
		# input
		x = tf.placeholder(tf.float32, [None, xCount])
		
		# hidden 1
		h1Count = int((xCount-yCount) * 0.75 * xx + yCount)
		w1 = self.getWeights(xCount, h1Count)
		b1 = self.getBiases(h1Count)
		h1 = tf.nn.relu(tf.matmul(x, w1) + b1)
		
		# hidden 2
		h2Count = int((xCount-yCount) * 0.50 * xx + yCount)
		w2 = self.getWeights(h1Count, h2Count)
		b2 = self.getBiases(h2Count)
		h2 = tf.nn.relu(tf.matmul(h1, w2) + b2)
		
		# hidden 3
		h3Count = int((xCount-yCount) * 0.25 * xx + yCount)
		w3 = self.getWeights(h2Count, h3Count)
		b3 = self.getBiases(h3Count)
		h3 = tf.nn.relu(tf.matmul(h2, w3) + b3)
		
		"""# hidden 4
		w4 = self.getWeights(HIDDEN_NODES, HIDDEN_NODES)
		b4 = self.getBiases(HIDDEN_NODES)
		hN = tf.nn.relu(tf.matmul(h3, w4) + b4)"""
		
		# output
		W_logits = tf.Variable(tf.truncated_normal([h3Count, yCount] , stddev=0.1))
		b_logits = tf.Variable(tf.zeros([yCount]))
		logits = tf.matmul(h3, W_logits) + b_logits
		y = tf.nn.softmax(logits)
		#y = logits
		
		# clean prediction
		#ones = tf.ones([raceCount], tf.int64)
		#prediction = tf.add(tf.argmax(y,1), ones)
		
		# wanted output
		yWanted = tf.placeholder(tf.float32, [None, yCount])

		# error
		#cross_entropy = tf.nn.softmax_cross_entropy_with_logits(logits, yWanted)
		#loss = tf.reduce_mean(cross_entropy)
		#loss = 0.1		
		diff = tf.reduce_sum(tf.abs(tf.sub(y, yWanted)))
		s = tf.reduce_sum(yWanted)
		loss = tf.truediv(diff, s)

		# training
		train_op = tf.train.GradientDescentOptimizer(factor).minimize(loss)
		
		# eval
		correct_prediction = tf.equal(tf.argmax(y,1), tf.argmax(yWanted,1))
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
		
		#stuff

		# init
		init_op = tf.initialize_all_variables()
		sess = tf.Session()
		sess.run(init_op)
		
		# train
		s = 200
		for i in range(10000000):
			xBatch, yBatch = self.data.nextBacthWin(batchSize)
			_, loss_val = sess.run([train_op, loss], feed_dict={x: xBatch, yWanted: yBatch})
			if i % (s*50) == 0:
				print('Step\t| Loss\t\t| Train\t\t|\t       \t| Test\t\t|\t   ')
			if i % s == 0:
				accuracyValueTrain = sess.run(accuracy, feed_dict={x: self.data.training['input'], yWanted: self.data.training['win']})
				diffTrain = sess.run(diff, feed_dict={x: self.data.training['input'], yWanted: self.data.training['win']})
				accuracyValueTest = sess.run(accuracy, feed_dict={x: self.data.test['input'], yWanted: self.data.test['win']})
				diffTest = sess.run(diff, feed_dict={x: self.data.test['input'], yWanted: self.data.test['win']})
				lossTrain = sess.run(loss, feed_dict={x: self.data.test['input'], yWanted: self.data.test['win']})
				print("%7d\t|" % i, 
					"\t%4.4f\t|" % lossTrain,
					"\t%4.4f\t|" % accuracyValueTrain, 
					"\t%4.2f\t|" % diffTrain,
					"\t%4.4f\t|" % accuracyValueTest,
					"\t%4.2f" % diffTest,
					)
		sess.close()
	
	def getWeights(self, i, o):
		return tf.Variable(tf.truncated_normal([i, o], 
				stddev = 1.0 / math.sqrt(float(i))))
	
	def getBiases(self, c):
		return tf.Variable(tf.zeros([c]))
		
		
	
		
	

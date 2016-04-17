from datamanager.conf import Conf
import numpy as np

class Data:
	def __init__(self, start, end):
		self.MAX_TEAMS = 30
		self.INPUTS_PER_TEAMS = 12
		self.inputs = self.getInputs(start, end)
		self.win = self.getWinOutputs(start, end)
		self.show = self.getShowOutputs(start, end)
		self.batchStart = 0
		self.size = len(self.show)
	
	def nextBacthWin(self, size):
		start = self.batchStart
		end = (self.batchStart + size) % self.size
		self.batchStart = end
		if(start < end):
			return self.inputs[start:end], self.win[start:end]
		else:
			return self.inputs[start:], self.win[start:]

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

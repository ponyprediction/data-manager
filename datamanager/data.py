from datamanager.conf import Conf
import numpy as np

class Data:
	def __init__(self, start, end):
		self.MIN_TEAMS = 0
		self.MAX_TEAMS = 20
		self.INPUTS_PER_TEAMS = 15
		
		a = 0.0
		b = 0.8
		c = 1.0
		
		self.training = self.getData(start, end, a, b)
		self.test = self.getData(start, end, b, c)
		
		self.batchStart = 0
		self.size = len(self.training['input'])
		
		print(self.size)
	
	def nextBacthWin(self, size):
		start = self.batchStart
		end = (self.batchStart + size) % self.size
		self.batchStart = end
		if(start < end):
			return self.training['input'][start:end], self.training['win'][start:end]
		else:
			return self.training['input'][start:], self.training['win'][start:]
	
	def nextBacthShow(self, size):
		start = self.batchStart
		end = (self.batchStart + size) % self.size
		self.batchStart = end
		if(start < end):
			return self.training['input'][start:end], self.training['show'][start:end]
		else:
			return self.training['input'][start:], self.training['show'][start:]
	
	
	def getData(self, startDay, endDay, startArray, endArray):
		inputs = []
		wins = []
		shows = []
		fnameInputs = Conf.TRAINING_SET_INPUTS.replace('START',startDay).replace('END',endDay)
		fnameWins = Conf.TRAINING_SET_WINS.replace('START',startDay).replace('END',endDay)
		fnameShows = Conf.TRAINING_SET_SHOWS.replace('START',startDay).replace('END',endDay)
		with open(fnameInputs, 'r') as fIn, open(fnameWins, 'r') as fW, open(fnameShows, 'r') as fS:
			for lIn, lW, lS in zip(fIn, fW, fS):
				# inputs
				a = [float(x) for x in lIn.split(';')]
				if len(a) not in range(self.MIN_TEAMS*self.INPUTS_PER_TEAMS, self.MAX_TEAMS*self.INPUTS_PER_TEAMS+1): # if not right team count we don't add it
					continue
				while(len(a) < self.MAX_TEAMS*self.INPUTS_PER_TEAMS):
					a.append(0.0)
				inputs.append(a[:self.MAX_TEAMS*self.INPUTS_PER_TEAMS])
				# wins
				a = []
				list = [(int(x) if x!='\n' else 0) for x in lW.split(';')]
				for i in range(1, self.MAX_TEAMS+1):
					if i in list:
						a.append(1.0)
					else:
						a.append(0.0)
				wins.append(a[:self.MAX_TEAMS])
				# shows
				a = []
				list = [(int(x) if x!='\n' else 0) for x in lS.split(';')]
				for i in range(1, self.MAX_TEAMS+1):
					if i in list:
						a.append(1.0)
					else:
						a.append(0.0)
				shows.append(a[:self.MAX_TEAMS])
		#
		size = float(len(inputs))
		startArray = int(size * startArray)
		endArray = int(size * endArray)
		inputs = np.array(inputs[startArray:endArray])
		wins = np.array(wins[startArray:endArray])
		shows = np.array(shows[startArray:endArray])
		#
		return {'input':inputs, 'win':wins, 'show':shows}
		
	
	
	
	
	"""def getInputs(self, startDay, endDay, startArray, endArray):
		inputs = []
		fname = Conf.TRAINING_SET_INPUTS.replace('START',startDay).replace('END',endDay)
		with open(fname, 'r') as f:
			for line in f:
				a = [float(x) for x in line.split(';')]
				while(len(a) < self.MAX_TEAMS*self.INPUTS_PER_TEAMS):
					a.append(0.0)
				inputs.append(a[:self.MAX_TEAMS*self.INPUTS_PER_TEAMS])
		size = float(len(inputs))
		startArray = int(size * startArray)
		endArray = int(size * endArray)
		inputs = np.array(inputs[startArray:endArray])
		return inputs
	
	def getWinOutputs(self, startDay, endDay, startArray, endArray):
		outputs = []
		fname = Conf.TRAINING_SET_WINS.replace('START',startDay).replace('END',endDay)
		with open(fname, 'r') as f:
			for line in f:
				list = [(int(x) if x!='\n' else 0) for x in line.split(';')]
				a = []
				for i in range(1, self.MAX_TEAMS+1):
					if i in list:
						a.append(1.0)
					else:
						a.append(0.0)
				outputs.append(a[:self.MAX_TEAMS])
		size = float(len(outputs))
		startArray = int(size * startArray)
		endArray = int(size * endArray)
		outputs = np.array(outputs[startArray:endArray])
		return outputs
		
	def getShowOutputs(self, startDay, endDay, startArray, endArray):
		outputs = []
		fname = Conf.TRAINING_SET_SHOWS.replace('START',startDay).replace('END',endDay)
		with open(fname, 'r') as f:
			for line in f:
				list = [(int(x) if x!='\n' else 0) for x in line.split(';')]
				a = []
				for i in range(1, self.MAX_TEAMS+1):
					if i in list:
						a.append(1.0)
					else:
						a.append(0.0)
				outputs.append(a[:self.MAX_TEAMS])
		size = float(len(outputs))
		startArray = int(size * startArray)
		endArray = int(size * endArray)
		outputs = np.array(outputs[startArray:endArray])
		return outputs"""

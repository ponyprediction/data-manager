from conf import Conf
from parser import Parser
import datetime
import sys

class Inserter:
	def __init__(self, start, end, force = False):
		self.start = datetime.datetime.strptime(start, '%Y-%m-%d').date()
		self.end = datetime.datetime.strptime(end, '%Y-%m-%d').date()
		self.force = force
		
	def insert(self):
		print 'Insert from ' + self.start.strftime('%Y-%m-%d') + ' to ' + self.end.strftime('%Y-%m-%d')
		date = self.start
		day = datetime.timedelta(days=1)
		while date <= self.end:
			reunions = Parser.getReunions(date)
			for reunion in reunions:
				races = Parser.getRaces(date, reunion['localId'])
				for race in races:
					self.insertRace(date, reunion['localId'], race['localId'])
			date = date + day
		self.overwrite('')
		print '\rDone'
		
	def insertRace(self, date, reunion, localId):
		raceId = date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(localId)
		self.overwrite(raceId)
		horsesStart = Parser.getHorsesStart(date, reunion, localId)
		horsesChoice = Parser.getHorsesChoice(date, reunion, localId)
		jockeysStart = Parser.getJockeysStart(date, reunion, localId)
		trainersStart = Parser.getTrainersStart(date, reunion, localId)
		array = []
		for i, value in enumerate(horsesStart):
			id = horsesStart[i]['id']
			prediction = None
			for x in horsesChoice:
				if x['id'] == id:
					prediction = x['place']
					break
			array.append({'id':id, 
				'prediction':prediction, 
				'horse':horsesStart[i]['name'], 
				'gender':horsesStart[i]['gender'], 
				'age':horsesStart[i]['age'],
				'jockey':jockeysStart[i]['name'],
				'trainer':trainersStart[i]['name']
			})
		return array
	
	def overwrite(self, m):
		sys.stdout.write('\r')
		for x in range(0, 80):
			sys.stdout.write(' ')
		sys.stdout.write('\r' + m)
		sys.stdout.flush()

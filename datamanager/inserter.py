from datamanager.conf import Conf
from datamanager.parser import Parser
import datetime
import sys
from pprint import pprint

class Inserter:
	def __init__(self, start, end, force = False):
		self.start = datetime.datetime.strptime(start, '%Y-%m-%d').date()
		self.end = datetime.datetime.strptime(end, '%Y-%m-%d').date()
		self.force = force
		
	def insert(self):
		print('Insert from ' + self.start.strftime('%Y-%m-%d') + ' to ' + self.end.strftime('%Y-%m-%d'))
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
		print('\rDone')
		
	def insertRace(self, date, reunion, race):
		raceId = date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(race)
		self.overwrite(raceId)
		data = Parser.getRaceData(date, reunion, race)
		return data
	
	def overwrite(self, m):
		sys.stdout.write('\r')
		for x in range(0, 80):
			sys.stdout.write(' ')
		sys.stdout.write('\r' + m)
		sys.stdout.flush()

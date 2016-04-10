from datamanager.conf import Conf
from datamanager.parser import Parser
import datetime
import sys
from pprint import pprint
import mysql.connector

class Inserter:
	def __init__(self, start, end, force = False):
		self.start = datetime.datetime.strptime(start, '%Y-%m-%d').date()
		self.end = datetime.datetime.strptime(end, '%Y-%m-%d').date()
		self.force = force
		self.database = mysql.connector.connect(user='ponyprediction', 
				password='ponyprediction',
				host='localhost',
				database='ponyprediction')
		self.c = 0
				
	def __del__(self):
		print(self.c)
		self.database.close()
		
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
		self.overwrite(date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(race))
		raceId = date.strftime('%Y-%m-%d') + str(reunion) + str(race)
		data = Parser.getRaceData(date, reunion, race)
		for team in data['teams']:
			horseId = self.insertHorse(team['age'], team['gender'], team['horse'])
			jockeyId = self.insertJockey(team['jockey'])
			trainerId = self.insertTrainer(team['trainer'])
			self.insertTeam(horseId, jockeyId, trainerId, team)
			self.c = self.c + 1
		return data
	
	def insertTeam(self, horseId, jockeyId, trainerId, team):
		cursor = self.database.cursor()
		request = ("""INSERT INTO teams 
				(horseId, jockeyId, trainerId, 
					start, prediction, arrival,
					odds1, odds2, odds3,
					firstMoney, secondMoney, 
					fourthMoney, showMoney)
				VALUES (%s, %s, %s, %s, %s, %s,
					%s, %s, %s, %s, %s, %s, %s);""")
		data = (horseId, jockeyId, trainerId, 
				team['start'], team['prediction'], team['arrival'],
				team['odds1'], team['odds2'], team['odds3'],
				team['firstMoney'], team['secondMoney'], 
				team['fourthMoney'], team['showMoney'])
		cursor.execute(request, data)
		cursor.close()
			
	def insertHorse(self, age, gender, name):
		cursor = self.database.cursor()
		cursor.execute('SELECT COUNT(*) '
				'FROM horses '
				'WHERE name=%s',(name,))
		if not cursor.fetchone()[0]:
			request = ("""INSERT INTO horses
					(age, gender, name) 
					VALUES (%s, %s, %s);""")
			data = (age, gender, name)
			try:
			    cursor.execute(request, data)
			    self.database.commit()
			except:
			    print(cursor.statement)
			    raise
		cursor.execute('SELECT id '
				'FROM horses '
				'WHERE name=%s',(name,))
		id = cursor.fetchone()[0]
		cursor.close()
		return id
	
	def insertJockey(self, name):
		cursor = self.database.cursor()
		cursor.execute('SELECT COUNT(*) '
				'FROM jockeys '
				'WHERE name=%s',(name,))
		if not cursor.fetchone()[0]:
			request = ("INSERT INTO jockeys "
					"(name) "
					'VALUES ("' + name + '");')
			try:
			    cursor.execute(request)
			    self.database.commit()
			except:
			    print(cursor.statement)
			    raise
		cursor.execute('SELECT id '
				'FROM jockeys '
				'WHERE name=%s',(name,))
		id = cursor.fetchone()[0]
		cursor.close()
		return id
	
	def insertTrainer(self, name):
		cursor = self.database.cursor()
		cursor.execute('SELECT COUNT(*) '
				'FROM trainers '
				'WHERE name=%s',(name,))
		if not cursor.fetchone()[0]:
			request = ("INSERT INTO trainers "
					"(name) "
					'VALUES ("' + name + '");')
			try:
			    cursor.execute(request)
			    self.database.commit()
			except:
			    print(cursor.statement)
			    raise
		cursor.execute('SELECT id '
				'FROM trainers '
				'WHERE name=%s',(name,))
		id = cursor.fetchone()[0]
		cursor.close()
		return id
	
	def overwrite(self, m):
		sys.stdout.write('\r')
		for x in range(0, 80):
			sys.stdout.write(' ')
		sys.stdout.write('\r' + m)
		sys.stdout.flush()

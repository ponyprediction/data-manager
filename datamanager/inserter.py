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
				
	def __del__(self):
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
		raceTextId = date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(race)
		data = Parser.getRaceData(date, reunion, race)
		teams = []
		for team in data['teams']:
			horseId = self.insertHorse(team['age'], team['gender'], team['horse'])
			jockeyId = self.insertJockey(team['jockey'])
			trainerId = self.insertTrainer(team['trainer'])
			teams.append(self.insertTeam(raceTextId, horseId, jockeyId, trainerId, team))
		raceId = self.insertRace2(raceTextId, date, reunion, race, len(teams))
		#self.insertTeamsInRaces(teams, raceId)
		#return data
	
	
	def insertRace2(self, textId, date, teamCount):
		cursor = self.database.cursor()
		cursor.execute('SELECT COUNT(*) '
				'FROM races '
				'WHERE (textId=%s)',(textId,))
		if not cursor.fetchone()[0]:
			request = ('INSERT INTO teams '
					'(textId, date, teamCount, length, type) '
					'VALUES (%s, %s, %s, %s, %s);')
			data = (textId, date, teamCount, 0, 0)
			try:
				cursor.execute(request, data)
				self.database.commit()
			except:
			    print(cursor.statement)
			    raise
		cursor.execute('SELECT id '
				'FROM races '
				'WHERE (textId=%s)',(textId,))
		id = cursor.fetchone()[0]
		cursor.close()
		return id
	
	def insertTeamsInRaces(self, teams, raceId):
		cursor = self.database.cursor()
		for teamId in teams:
			cursor.execute('SELECT COUNT(*) '
					'FROM teamsInRaces '
					'WHERE (raceId=%s AND teamId=%s)',(raceId, teamId,))
			if not cursor.fetchone()[0]:
				request = ('INSERT INTO teamsInRaces '
						'(age, gender, name) '
						'VALUES (%s, %s, %s);')
				data = (raceId, teamId,)
				try:
				    cursor.execute(request, data)
				    self.database.commit()
				except:
				    print(cursor.statement)
				    raise
		cursor.close()
			
			
	
	def insertTeam(self, raceId, horseId, jockeyId, trainerId, team):
		cursor = self.database.cursor()
		cursor.execute('SELECT COUNT(*) '
				'FROM teams '
				'WHERE (raceId=%s AND horseId=%s AND jockeyId=%s AND trainerId=%s)',(raceId, horseId, jockeyId, trainerId,))
		if not cursor.fetchone()[0]:
			request = ("""INSERT INTO teams 
					(raceId, horseId, jockeyId, trainerId, 
						start, prediction, arrival,
						odds1, odds2, odds3,
						firstMoney, secondMoney, 
						fourthMoney, showMoney)
					VALUES (%s, %s, %s, %s, %s, %s, %s,
						%s, %s, %s, %s, %s, %s, %s);""")
			data = (raceId, horseId, jockeyId, trainerId, 
					team['start'], team['prediction'], team['arrival'],
					team['odds1'], team['odds2'], team['odds3'],
					team['firstMoney'], team['secondMoney'], 
					team['fourthMoney'], team['showMoney'])
			try:
				cursor.execute(request, data)
				self.database.commit()
			except:
			    print(cursor.statement)
			    raise
		cursor.execute('SELECT id '
				'FROM teams '
				'WHERE (raceId=%s AND horseId=%s AND jockeyId=%s AND trainerId=%s)',(raceId, horseId, jockeyId, trainerId,))
		id = cursor.fetchone()[0]
		cursor.close()
		return id
			
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

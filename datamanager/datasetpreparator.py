import mysql.connector
import datetime
from pprint import pprint
from datamanager.database import Database

class DatasetPreparator:
	def __init__(self):
		self.database = mysql.connector.connect(user='ponyprediction', 
				password='ponyprediction',
				host='localhost',
				database='ponyprediction')
				
	def __del__(self):
		self.database.close()
	
	def getTrainingSet(self, start, end):
		start = datetime.datetime.strptime(start, '%Y-%m-%d').date()
		end = datetime.datetime.strptime(end, '%Y-%m-%d').date()
		date = start
		day = datetime.timedelta(days=1)
		data = []
		while date <= end:
			print(date)
			data.append(self.getDataForDate(date.strftime('%Y-%m-%d')))
			date = date + day
		return data
	
	def getDataForDate(self, date):
		cursor = self.database.cursor()
		cursor.execute("""select id 
				from races
				where (date=%s);""",
				(date,));
		raceIds = []
		for (id,) in cursor:
			raceIds.append(id)
		cursor.close();
		data = []
		for raceId in raceIds:	
			data.append(self.getDataForRace(raceId, date))
		return data
	
	def getDataForRace(self, raceId, date):
		cursor = self.database.cursor()
		cursor.execute('''select teamId 
				from teamsInRaces
				where (raceId=%s);''',
				(raceId,));
		teamIds = []
		for (teamId,) in cursor:
			teamIds.append(teamId)
		cursor.close();
		data = []
		for teamId in teamIds:	
			data.append(self.getDataForTeam(teamId, date))
		return data
			
	def getDataForTeam(self, teamId, date):
		trainerIds = Database.getTrainersForTeam(teamId)
		data = []
		for trainerId in trainerIds:
			data.extend(self.getDataForTrainer(trainerId, date))
		return data
			
	def getDataForTrainer(self, trainerId, date):
		raceCount = float(Database.getRaceCountTrainerBefore(trainerId, date))
		race1 = float(Database.getRaceCountAtArrivalByTrainerBefore(trainerId, date, '1'))
		race2 =  float(Database.getRaceCountAtArrivalByTrainerBefore(trainerId, date, '2'))
		race3 = float(Database.getRaceCountAtArrivalByTrainerBefore(trainerId, date, '3'))
		
		percent1 = race1 / raceCount
		percent2 = race2 / raceCount
		percent3 = race3 / raceCount
		
		percentShow = (race1+race2+race3) / raceCount
		
		return [trainerId, raceCount, percent1, percent2, percent3, percentShow]
	
		
		
	

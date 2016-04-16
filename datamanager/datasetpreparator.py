import mysql.connector
import datetime
from pprint import pprint
from datamanager.database import Database
from datamanager.conf import Conf

class DatasetPreparator:
	def __init__(self):
		self.database = mysql.connector.connect(user='ponyprediction', 
				password='ponyprediction',
				host='localhost',
				database='ponyprediction')
				
	def __del__(self):
		self.database.close()
	
	def saveTrainingSet(self, start, end):
		data = self.getTrainingSet(start, end)
		inputs = wins = shows = ''
		for day in data:
			for race in day:
				wins = wins + ';'.join(str(x) for x in race[0]) + '\n'
				shows = shows + ';'.join(str(x) for x in race[1]) + '\n'
				for id, team in enumerate(race[2]):
					if id != 0:
						inputs =  inputs + ';'
					inputs = inputs + ';'.join(str(x) for x in team) 
				inputs  = inputs + '\n'
		fname = Conf.TRAINING_SET_WINS.replace('START',start).replace('END',end)
		f = open(fname, 'w')
		f.write(wins)
		f.close()
		fname = Conf.TRAINING_SET_SHOWS.replace('START',start).replace('END',end)
		f = open(fname, 'w')
		f.write(shows)
		f.close()
		fname = Conf.TRAINING_SET_INPUTS.replace('START',start).replace('END',end)
		f = open(fname, 'w')
		f.write(inputs)
		f.close()
	
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
			print(raceId)
			data.append(self.getDataForRace(raceId, date))
		return data
	
	def getDataForRace(self, raceId, date):
		cursor = self.database.cursor()
		cursor.execute('''SELECT teams.id
				FROM teams, teamsInRaces
				WHERE (teams.id = teamsInRaces.teamId
					AND teamsInRaces.raceId = %s)
				ORDER BY teams.start ASC''',
				(raceId,));
		teamIds = []
		for (teamId,) in cursor:
			teamIds.append(teamId)
		cursor.close();
		inputs = []
		winners = Database.getWinners(raceId)
		shows = Database.getShows(raceId)
		for (teamId) in teamIds:
			inputs.append(self.getDataForTeam(teamId, date))
		return [winners, shows, inputs]
			
	def getDataForTeam(self, teamId, date):
		data = []
		trainerIds = Database.getMembersInTeam(teamId)
		for (horseId, jockeyId, trainerId) in trainerIds:
			data.extend(self.getDataForHorse(horseId, date))
			data.extend(self.getDataForJockey(jockeyId, date))
			data.extend(self.getDataForTrainer(trainerId, date))
		return data
	
	def getDataForHorse(self, horseId, date):
		raceCount = float(Database.getRaceCountHorseBefore(horseId, date))
		race1 = float(Database.getRaceCountAtArrivalByHorseBefore(horseId, date, '1'))
		race2 =  float(Database.getRaceCountAtArrivalByHorseBefore(horseId, date, '2'))
		race3 = float(Database.getRaceCountAtArrivalByHorseBefore(horseId, date, '3'))
		percent1 = race1 / raceCount if raceCount else 0
		percent2 = race2 / raceCount if raceCount else 0
		percent3 = race3 / raceCount if raceCount else 0
		percentShow = (race1+race2+race3) / raceCount if raceCount else 0
		return [raceCount, percent1, percent2, percent3, percentShow]
	
	def getDataForJockey(self, jockeyId, date):
		raceCount = float(Database.getRaceCountJockeyBefore(jockeyId, date))
		race1 = float(Database.getRaceCountAtArrivalByJockeyBefore(jockeyId, date, '1'))
		race2 =  float(Database.getRaceCountAtArrivalByJockeyBefore(jockeyId, date, '2'))
		race3 = float(Database.getRaceCountAtArrivalByJockeyBefore(jockeyId, date, '3'))
		percent1 = race1 / raceCount if raceCount else 0
		percent2 = race2 / raceCount if raceCount else 0
		percent3 = race3 / raceCount if raceCount else 0
		percentShow = (race1+race2+race3) / raceCount if raceCount else 0
		return [raceCount, percent1, percent2, percent3, percentShow]
	
			
	def getDataForTrainer(self, trainerId, date):
		raceCount = float(Database.getRaceCountTrainerBefore(trainerId, date))
		race1 = float(Database.getRaceCountAtArrivalByTrainerBefore(trainerId, date, '1'))
		race2 =  float(Database.getRaceCountAtArrivalByTrainerBefore(trainerId, date, '2'))
		race3 = float(Database.getRaceCountAtArrivalByTrainerBefore(trainerId, date, '3'))
		percent1 = race1 / raceCount if raceCount else 0
		percent2 = race2 / raceCount if raceCount else 0
		percent3 = race3 / raceCount if raceCount else 0
		percentShow = (race1+race2+race3) / raceCount if raceCount else 0
		return [raceCount, percent1, percent2, percent3, percentShow]
	
		
		
	

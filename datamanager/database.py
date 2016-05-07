import mysql.connector
from datamanager.conf import Conf

class Database:
	connection = mysql.connector.connect(user=Conf.DATABASE_USER, 
				password=Conf.DATABASE_PASSWORD,
				host=Conf.DATABASE_URL,
				database=Conf.DATABASE_NAME)
	"""
		Horse
	"""
	@staticmethod
	def getRaceCountHorse(horseId, start, end):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.horseId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId
					AND races.date > %s
					AND races.date < %s);''',
				(horseId,start,end,));
		return str(cursor.fetchone()[0])
	
	@staticmethod
	def getRaceCountAtArrivalByHorse(horseId, arrival, start, end):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.horseId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId 
					AND teams.arrival = %s
					AND races.date > %s
					AND races.date < %s);''',
				(horseId, arrival, start, end,));
		return str(cursor.fetchone()[0])
	
	"""
		Jockey
	"""
	@staticmethod
	def getRaceCountJockey(jockeyId, start, end):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.jockeyId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId
					AND races.date > %s
					AND races.date < %s);''',
				(jockeyId, start, end,));
		return str(cursor.fetchone()[0])
	
	@staticmethod
	def getRaceCountAtArrivalByJockey(jockeyId, arrival, start, end):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.jockeyId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId 
					AND teams.arrival = %s
					AND races.date > %s
					AND races.date < %s);''',
				(jockeyId,arrival,start, end, ));
		return str(cursor.fetchone()[0])
	"""
		Trainer
	"""
	@staticmethod
	def getRaceCountTrainer(trainerId, start, end):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.trainerId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId
					AND races.date > %s
					AND races.date < %s);''',
				(trainerId,start, end, ));
		return str(cursor.fetchone()[0])
	
	@staticmethod
	def getRaceCountAtArrivalByTrainer(trainerId, arrival, start, end):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.trainerId = %s
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId 
					AND teams.arrival = %s
					AND races.date > %s
					AND races.date < %s);''',
				(trainerId, arrival, start, end));
		return str(cursor.fetchone()[0])
	
	"""
		Other
	"""
	@staticmethod
	def getMembersInTeam(teamId):
		cursor = Database.connection.cursor()
		cursor.execute('''select horseId, jockeyId, trainerId 
				from teams
				where (id=%s);''',
				(teamId,));
		members = []
		for (horseId, jockeyId, trainerId,) in cursor:
			members.append([horseId, jockeyId, trainerId])
		cursor.close()
		return members
	
	@staticmethod
	def getWinners(raceId):
		cursor = Database.connection.cursor()
		cursor.execute('''select teams.start, teams.firstMoney
				from teamsInRaces, teams, races
				where (teamsInRaces.raceId = %s
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId  
					AND teams.firstMoney > 0);''',
				(raceId,));
		starts = []
		for ((start,firstMoney,)) in cursor:
			starts.append(str(start) + ':' + str(firstMoney))
		return starts
	
	@staticmethod
	def getShows(raceId):
		cursor = Database.connection.cursor()
		cursor.execute('''select teams.start, teams.showMoney
				from teamsInRaces, teams, races
				where (teamsInRaces.raceId = %s
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId
					AND teams.showMoney > 0);''',
				(raceId,));
		starts = []
		for ((start,showMoney,)) in cursor:
			starts.append(str(start) + ':' + str(showMoney))
		return starts
	
	@staticmethod
	def getOdds(teamId):
		cursor = Database.connection.cursor()
		cursor.execute('''select teams.odds1, teams.odds2, teams.odds3
				from teams
				where teams.id = %s
				limit 1;''',
				(teamId,));
		odds = []
		for (odds1,odds2,odds3,) in cursor:
			odds.extend([odds1, odds2, odds3])
		return odds
	
	
	
	
	
	
	
	
	
	
	
	
	

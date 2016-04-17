import mysql.connector

class Database:
	connection = mysql.connector.connect(user='ponyprediction', 
				password='ponyprediction',
				host='localhost',
				database='ponyprediction')
	"""
		Horse
	"""
	@staticmethod
	def getRaceCountHorseBefore(horseId, date):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.horseId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId
					AND races.date < %s);''',
				(horseId,date,));
		return str(cursor.fetchone()[0])
	
	@staticmethod
	def getRaceCountAtArrivalByHorseBefore(horseId, date, arrival):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.horseId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId 
					AND races.date < %s
					AND teams.arrival = %s);''',
				(horseId,date,arrival,));
		return str(cursor.fetchone()[0])
	
	"""
		Jockey
	"""
	@staticmethod
	def getRaceCountJockeyBefore(jockeyId, date):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.jockeyId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId
					AND races.date < %s);''',
				(jockeyId,date,));
		return str(cursor.fetchone()[0])
	
	@staticmethod
	def getRaceCountAtArrivalByJockeyBefore(jockeyId, date, arrival):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.jockeyId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId 
					AND races.date < %s
					AND teams.arrival = %s);''',
				(jockeyId,date,arrival,));
		return str(cursor.fetchone()[0])
	"""
		Trainer
	"""
	@staticmethod
	def getRaceCountTrainerBefore(trainerId, date):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.trainerId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId
					AND races.date < %s);''',
				(trainerId,date,));
		return str(cursor.fetchone()[0])
	
	@staticmethod
	def getRaceCountAtArrivalByTrainerBefore(trainerId, date, arrival):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.trainerId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId 
					AND races.date < %s
					AND teams.arrival = %s);''',
				(trainerId,date,arrival,));
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
		cursor.execute('''select teams.start
				from teamsInRaces, teams, races
				where (teamsInRaces.raceId = %s
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId  
					AND teams.firstMoney > 0);''',
				(raceId,));
		starts = []
		for (start,) in cursor:
			starts.append(start)
		return starts
	
	
	@staticmethod
	def getShows(raceId):
		cursor = Database.connection.cursor()
		cursor.execute('''select teams.start
				from teamsInRaces, teams, races
				where (teamsInRaces.raceId = %s
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId
					AND teams.showMoney > 0);''',
				(raceId,));
		starts = []
		for (start,) in cursor:
			starts.append(start)
		return starts
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
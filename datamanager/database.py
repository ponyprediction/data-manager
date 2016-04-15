import mysql.connector

class Database:
	connection = mysql.connector.connect(user='ponyprediction', 
				password='ponyprediction',
				host='localhost',
				database='ponyprediction')
	
	@staticmethod
	def getRaceCountTrainerBefore(trainerId, date):
		cursor = Database.connection.cursor()
		cursor.execute('''select COUNT(*)
				from teams, teamsInRaces, races
				where (teams.trainerId=%s 
					AND teams.id = teamsInRaces.teamId 
					AND races.id = teamsInRaces.raceId
					AND (races.date BETWEEN '0000-00-00' AND %s));''',
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
					AND (races.date BETWEEN '0000-00-00' AND %s)
					AND teams.arrival = %s);''',
				(trainerId,date,arrival,));
		return str(cursor.fetchone()[0])
	
	@staticmethod
	def getTrainersForTeam(teamId):
		cursor = Database.connection.cursor()
		cursor.execute('''select trainerId 
				from teams
				where (id=%s);''',
				(teamId,));
		trainerIds = []
		for (trainerId,) in cursor:
			trainerIds.append(trainerId)
		cursor.close();
		return trainerIds

import mysql.connector

print("bob")

database = mysql.connector.connect(user='ponyprediction', 
		password='ponyprediction',
		host='localhost',
		database='ponyprediction')


		
database.close()

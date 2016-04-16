import unittest
from datamanager.datasetpreparator import DatasetPreparator
import datetime
from pprint import pprint



class TestDatasetPreparato(unittest.TestCase):
	
	def test_getTrainingSet(self):
		start = '2016-03-31'
		end = '2016-03-31'
		data = DatasetPreparator().getTrainingSet(start, end)
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
		f = open('wins', 'w')
		f.write(wins)
		f.close()
		f = open('shows', 'w')
		f.write(shows)
		f.close()
		f = open('inputs', 'w')
		f.write(inputs)
		f.close()
	
	def test_getDataForRace(self):
		date = '2016-03-01'
		raceId = 2600
		data = DatasetPreparator().getDataForRace(raceId, date)
		#pprint(data)

if __name__ == '__main__':
    unittest.main()

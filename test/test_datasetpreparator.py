import unittest
from datamanager.datasetpreparator import DatasetPreparator
import datetime
from pprint import pprint



class TestDatasetPreparato(unittest.TestCase):
	
	def test_getTrainingSet(self):
		start = '2016-03-31'
		end = '2016-03-31'
		data = DatasetPreparator().getTrainingSet(start, end)
		
	
	def test_getDataForRace(self):
		date = '2016-03-01'
		raceId = 2600
		data = DatasetPreparator().getDataForRace(raceId, date)
		#pprint(data)

if __name__ == '__main__':
    unittest.main()

import unittest
from datamanager.datasetpreparator import DatasetPreparator
import datetime
from pprint import pprint



class TestDatasetPreparato(unittest.TestCase):
	
	def test_getTrainingSet(self):
		test_response = 'lolol'
		start = '2016-03-31'
		end = '2016-03-31'
		response = DatasetPreparator().getTrainingSet(start, end)
		pprint(response)
		#self.assertEqual(response, test_response)

if __name__ == '__main__':
    unittest.main()

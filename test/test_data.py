import unittest
from datamanager.data import Data
import datetime
from pprint import pprint

class TestData(unittest.TestCase):
	
	def test_getData(self):
		data = Data('2015-01-01', '2015-01-01')
		pprint(data)

if __name__ == '__main__':
	unittest.main()


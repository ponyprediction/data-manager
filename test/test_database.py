import unittest
from datamanager.database import Database
import datetime
from pprint import pprint

class TestDatabase(unittest.TestCase):
	
	def test_getOdds(self):
		odds = Database.getOdds(1)
		pprint(odds)

if __name__ == '__main__':
	unittest.main()


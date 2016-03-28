import unittest
from ..src.parser import Parser
import datetime
from pprint import pprint



class TestParser(unittest.TestCase):
	
	def test_getReunions(self):
		test_reunions = [
			{'localId': 1, 'globalId': 29592}, 
			{'localId': 2, 'globalId': 29593}, 
			{'localId': 3, 'globalId': 29591}, 
			{'localId': 4, 'globalId': 29595}, 
			{'localId': 5, 'globalId': 29594}
		]
		date = '2016-01-01'
		reunions = Parser.getReunions(datetime.datetime.strptime(date, '%Y-%m-%d').date())
		self.assertEqual(reunions, test_reunions)
		
	def test_getRaces(self):
		test_races = [
			{'localId': 1, 'globalId': 169644},
			{'localId': 2, 'globalId': 169645},
			{'localId': 3, 'globalId': 169646},
			{'localId': 4, 'globalId': 169647},
			{'localId': 5, 'globalId': 169648},
			{'localId': 6, 'globalId': 169649},
			{'localId': 7, 'globalId': 169650},
			{'localId': 8, 'globalId': 169651},
			{'localId': 9, 'globalId': 169652}
		]
		date = '2016-01-01'
		reunionId = 1
		races = Parser.getRaces(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId)
		self.assertEqual(races, test_races)
	
	def test_getHorses(self):
		test_horses = [
			{'age': 5, 'gender': u'H', 'id': 1, 'name': u'BRAQUEUR DE BRAY'},
			{'age': 5, 'gender': u'H', 'id': 2, 'name': u'BLACK HOLE SUN'},
			{'age': 5, 'gender': u'H', 'id': 3, 'name': u'BLUEBERRY DE COUET'},
			{'age': 5, 'gender': u'M', 'id': 4, 'name': u'BOLIDE JIEL'},
			{'age': 5, 'gender': u'H', 'id': 5, 'name': u'BONCHAMP GEDE'},
			{'age': 5, 'gender': u'H', 'id': 6, 'name': u'BISTROT'},
			{'age': 5, 'gender': u'M', 'id': 7, 'name': u'BILBAO BOY'},
			{'age': 5, 'gender': u'H', 'id': 8, 'name': u'BALOU DU PAOU'},
			{'age': 5, 'gender': u'H', 'id': 9, 'name': u'BLASON DU BOSQUET'}
		]
		date = '2016-01-01'
		reunionId = 1
		raceId = 1
		horses = Parser.getHorses(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId, raceId)
		self.assertEqual(horses, test_horses)
			
if __name__ == '__main__':
    unittest.main()


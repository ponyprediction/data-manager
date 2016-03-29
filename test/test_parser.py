import unittest
from datamanager.parser import Parser
import datetime
from pprint import pprint



class TestParser(unittest.TestCase):
	
	def test_getReunions(self):
		test_reunions = [{'localId': 1, 'globalId': 29592}, 
			{'localId': 2, 'globalId': 29593}, 
			{'localId': 3, 'globalId': 29591}, 
			{'localId': 4, 'globalId': 29595}, 
			{'localId': 5, 'globalId': 29594}]
		date = '2016-01-01'
		reunions = Parser.getReunions(datetime.datetime.strptime(date, '%Y-%m-%d').date())
		self.assertEqual(reunions, test_reunions)
		
	def test_getRaces(self):
		test_races = [{'localId': 1, 'globalId': 169644},
			{'localId': 2, 'globalId': 169645},
			{'localId': 3, 'globalId': 169646},
			{'localId': 4, 'globalId': 169647},
			{'localId': 5, 'globalId': 169648},
			{'localId': 6, 'globalId': 169649},
			{'localId': 7, 'globalId': 169650},
			{'localId': 8, 'globalId': 169651},
			{'localId': 9, 'globalId': 169652}]
		date = '2016-01-01'
		reunionId = 1
		races = Parser.getRaces(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId)
		self.assertEqual(races, test_races)
	
	def test_getHorsesStart(self):
		test_horses = [{'age': 5, 'gender': u'H', 'id': 1, 'name': u'BRAQUEUR DE BRAY'},
			{'age': 5, 'gender': u'H', 'id': 2, 'name': u'BLACK HOLE SUN'},
			{'age': 5, 'gender': u'H', 'id': 3, 'name': u'BLUEBERRY DE COUET'},
			{'age': 5, 'gender': u'M', 'id': 4, 'name': u'BOLIDE JIEL'},
			{'age': 5, 'gender': u'H', 'id': 5, 'name': u'BONCHAMP GEDE'},
			{'age': 5, 'gender': u'H', 'id': 6, 'name': u'BISTROT'},
			{'age': 5, 'gender': u'M', 'id': 7, 'name': u'BILBAO BOY'},
			{'age': 5, 'gender': u'H', 'id': 8, 'name': u'BALOU DU PAOU'},
			{'age': 5, 'gender': u'H', 'id': 9, 'name': u'BLASON DU BOSQUET'}]
		date = '2016-01-01'
		reunionId = 1
		raceId = 1
		horses = Parser.getHorsesStart(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId, raceId)
		self.assertEqual(horses, test_horses)
	
	def test_getHorsesChoice(self):
		test_horses = [{'id': 7, 'name': u'BILBAO BOY', 'place': 1},
			{'id': 2, 'name': u'BLACK HOLE SUN', 'place': 2},
			{'id': 8, 'name': u'BALOU DU PAOU', 'place': 3},
			{'id': 5, 'name': u'BONCHAMP GEDE', 'place': 4},
			{'id': 9, 'name': u'BLASON DU BOSQUET', 'place': 5}]
		date = '2016-01-01'
		reunionId = 1
		raceId = 1
		horses = Parser.getHorsesChoice(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId, raceId)
		self.assertEqual(horses, test_horses)
		
	def test_getJockeysStart(self):
		test_jockeys = [{'id': 1, 'name': u'Desmarres Au.'},
			{'id': 2, 'name': u'Jublot Y.'},
			{'id': 3, 'name': u'Grimault A. Ph.'},
			{'id': 4, 'name': u'Rochard B.'},
			{'id': 5, 'name': u'Prioul F.'},
			{'id': 6, 'name': u'Mlle Le Coz Ch.'},
			{'id': 7, 'name': u'Jublot L.'},
			{'id': 8, 'name': u'Kondritz M.'},
			{'id': 9, 'name': u'Dromigny T.'}]
		date = '2016-01-01'
		reunionId = 1
		raceId = 1
		jockeys = Parser.getJockeysStart(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId, raceId)
		self.assertEqual(jockeys, test_jockeys)
		
	def test_getTrainersStart(self):
		test_array = [{'id': 1, 'name': u'Desmarres S.'},
			{'id': 2, 'name': u'Leblanc F.'},
			{'id': 3, 'name': u'Hubert A.'},
			{'id': 4, 'name': u'Dersoir J.L.'},
			{'id': 5, 'name': u'Sassier M.'},
			{'id': 6, 'name': u'Devouassoux Th.'},
			{'id': 7, 'name': u'Dreux Y.'},
			{'id': 8, 'name': u'Le Bezvoet Y.J.'},
			{'id': 9, 'name': u'Delacour G.'}]
		date = '2016-01-01'
		reunionId = 1
		raceId = 1
		array = Parser.getTrainersStart(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId, raceId)
		self.assertEqual(array, test_array)
	
	def test_getOdds(self):
		date = '2016-01-01'
		reunionId = 1
		raceId = 1
		array = Parser.getOdds(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId, raceId)
		pprint(array)
			
if __name__ == '__main__':
    unittest.main()


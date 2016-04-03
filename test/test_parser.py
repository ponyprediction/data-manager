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
		test_array = [{'id': 1, 'odds1': 29.6, 'odds2': 8.0, 'odds3': 20.2},
			{'id': 2, 'odds1': 5.3, 'odds2': 7.7, 'odds3': 5.0},
			{'id': 3, 'odds1': 10.9, 'odds2': 6.1, 'odds3': 7.8},
			{'id': 4, 'odds1': 8.2, 'odds2': 6.1, 'odds3': 6.1},
			{'id': 5, 'odds1': 17.8, 'odds2': 8.0, 'odds3': 11.8},
			{'id': 6, 'odds1': 26.0, 'odds2': 6.4, 'odds3': 11.8},
			{'id': 7, 'odds1': 4.4, 'odds2': 7.7, 'odds3': 5.4},
			{'id': 8, 'odds1': 4.9, 'odds2': 8.8, 'odds3': 5.4},
			{'id': 9, 'odds1': 4.5, 'odds2': 6.6, 'odds3': 5.6}]
		date = '2016-01-01'
		reunionId = 1
		raceId = 1
		array = Parser.getOdds(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId, raceId)
		self.assertEqual(array, test_array)
		
	def test_getArrival(self):
		test_array = [{'horse': u'BOLIDE JIEL', 'id': 4, 'place': 1},
			{'horse': u'BALOU DU PAOU', 'id': 8, 'place': 2},
			{'horse': u'BISTROT', 'id': 6, 'place': 3},
			{'horse': u'BLASON DU BOSQUET', 'id': 9, 'place': 4},
			{'horse': u'BONCHAMP GEDE', 'id': 5, 'place': 5},
			{'horse': u'BLUEBERRY DE COUET', 'id': 3, 'place': 6}]
		date = '2016-01-01'
		reunionId = 1
		raceId = 1
		array = Parser.getArrival(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId, raceId)
		self.assertEqual(array, test_array)

	def test_getMoney(self):
		test_array = [
			{'fourth': 0.0, 'id': 4, 'second': 0.0, 'show': 2.3, 'win': 8.2},
 			{'fourth': 0.0, 'id': 8, 'second': 5.4, 'show': 2.2, 'win': 0.0},
 			{'fourth': 0.0, 'id': 6, 'second': 0.0, 'show': 6.0, 'win': 0.0},
 			{'fourth': 6.6, 'id': 9, 'second': 0.0, 'show': 0.0, 'win': 0.0}]
		date = '2016-01-01'
		reunionId = 1
		raceId = 1
		array = Parser.getMoney(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId, raceId)
		self.assertEqual(array, test_array)
	
	def test_getArrival(self):
		test_array = {'teams': [{'prediction': None, 'odds2': 8.0, 'fourth': 0.0, 'second': 0.0, 'jockey': 'Desmarres Au.', 'win': 0.0, 'place': None, 'horse': 'BRAQUEUR DE BRAY', 'odds3': 20.2, 'id': 1, 'show': 0.0, 'age': 5, 'trainer': 'Desmarres S.', 'odds1': 29.6, 'gender': 'H'}, {'prediction': 2, 'odds2': 7.7, 'fourth': 0.0, 'second': 0.0, 'jockey': 'Jublot Y.', 'win': 0.0, 'place': None, 'horse': 'BLACK HOLE SUN', 'odds3': 5.0, 'id': 2, 'show': 0.0, 'age': 5, 'trainer': 'Leblanc F.', 'odds1': 5.3, 'gender': 'H'}, {'prediction': None, 'odds2': 6.1, 'fourth': 0.0, 'second': 0.0, 'jockey': 'Grimault A. Ph.', 'win': 0.0, 'place': 6, 'horse': 'BLUEBERRY DE COUET', 'odds3': 7.8, 'id': 3, 'show': 0.0, 'age': 5, 'trainer': 'Hubert A.', 'odds1': 10.9, 'gender': 'H'}, {'prediction': None, 'odds2': 6.1, 'fourth': 0.0, 'second': 0.0, 'jockey': 'Rochard B.', 'win': 8.2, 'place': 1, 'horse': 'BOLIDE JIEL', 'odds3': 6.1, 'id': 4, 'show': 2.3, 'age': 5, 'trainer': 'Dersoir J.L.', 'odds1': 8.2, 'gender': 'M'}, {'prediction': 4, 'odds2': 8.0, 'fourth': 0.0, 'second': 0.0, 'jockey': 'Prioul F.', 'win': 0.0, 'place': 5, 'horse': 'BONCHAMP GEDE', 'odds3': 11.8, 'id': 5, 'show': 0.0, 'age': 5, 'trainer': 'Sassier M.', 'odds1': 17.8, 'gender': 'H'}, {'prediction': None, 'odds2': 6.4, 'fourth': 0.0, 'second': 0.0, 'jockey': 'Mlle Le Coz Ch.', 'win': 0.0, 'place': 3, 'horse': 'BISTROT', 'odds3': 11.8, 'id': 6, 'show': 6.0, 'age': 5, 'trainer': 'Devouassoux Th.', 'odds1': 26.0, 'gender': 'H'}, {'prediction': 1, 'odds2': 7.7, 'fourth': 0.0, 'second': 0.0, 'jockey': 'Jublot L.', 'win': 0.0, 'place': None, 'horse': 'BILBAO BOY', 'odds3': 5.4, 'id': 7, 'show': 0.0, 'age': 5, 'trainer': 'Dreux Y.', 'odds1': 4.4, 'gender': 'M'}, {'prediction': 3, 'odds2': 8.8, 'fourth': 0.0, 'second': 5.4, 'jockey': 'Kondritz M.', 'win': 0.0, 'place': 2, 'horse': 'BALOU DU PAOU', 'odds3': 5.4, 'id': 8, 'show': 2.2, 'age': 5, 'trainer': 'Le Bezvoet Y.J.', 'odds1': 4.9, 'gender': 'H'}, {'prediction': 5, 'odds2': 6.6, 'fourth': 6.6, 'second': 0.0, 'jockey': 'Dromigny T.', 'win': 0.0, 'place': 4, 'horse': 'BLASON DU BOSQUET', 'odds3': 5.6, 'id': 9, 'show': 0.0, 'age': 5, 'trainer': 'Delacour G.', 'odds1': 4.5, 'gender': 'H'}], 'id': '2016-01-01-1-1'}
		date = '2016-01-01'
		reunionId = 1
		raceId = 1
		array = Parser.getRaceData(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId, raceId)
		self.assertEqual(array, test_array)
					
if __name__ == '__main__':
    unittest.main()


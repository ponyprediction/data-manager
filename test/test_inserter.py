import unittest
from datamanager.inserter import Inserter
import datetime
from pprint import pprint



class TestInserter(unittest.TestCase):
	
	def test_getHorsesChoice(self):
		#test_l = [{'trainer': u'Desmarres S.', 'horse': u'BRAQUEUR DE BRAY', 'jockey': u'Desmarres Au.', 'gender': u'H', 'age': 5, 'prediction': None, 'id': 1}, {'trainer': u'Leblanc F.', 'horse': u'BLACK HOLE SUN', 'jockey': u'Jublot Y.', 'gender': u'H', 'age': 5, 'prediction': 2, 'id': 2}, {'trainer': u'Hubert A.', 'horse': u'BLUEBERRY DE COUET', 'jockey': u'Grimault A. Ph.', 'gender': u'H', 'age': 5, 'prediction': None, 'id': 3}, {'trainer': u'Dersoir J.L.', 'horse': u'BOLIDE JIEL', 'jockey': u'Rochard B.', 'gender': u'M', 'age': 5, 'prediction': None, 'id': 4}, {'trainer': u'Sassier M.', 'horse': u'BONCHAMP GEDE', 'jockey': u'Prioul F.', 'gender': u'H', 'age': 5, 'prediction': 4, 'id': 5}, {'trainer': u'Devouassoux Th.', 'horse': u'BISTROT', 'jockey': u'Mlle Le Coz Ch.', 'gender': u'H', 'age': 5, 'prediction': None, 'id': 6}, {'trainer': u'Dreux Y.', 'horse': u'BILBAO BOY', 'jockey': u'Jublot L.', 'gender': u'M', 'age': 5, 'prediction': 1, 'id': 7}, {'trainer': u'Le Bezvoet Y.J.', 'horse': u'BALOU DU PAOU', 'jockey': u'Kondritz M.', 'gender': u'H', 'age': 5, 'prediction': 3, 'id': 8}, {'trainer': u'Delacour G.', 'horse': u'BLASON DU BOSQUET', 'jockey': u'Dromigny T.', 'gender': u'H', 'age': 5, 'prediction': 5, 'id': 9}]
		date = '2016-01-01'
		reunionId = 1
		raceId = 1
		l = Inserter(date, date).insertRace(datetime.datetime.strptime(date, '%Y-%m-%d').date(), reunionId, raceId)
		#pprint(l)
		#self.assertEqual(l, test_l)
			
if __name__ == '__main__':
    unittest.main()


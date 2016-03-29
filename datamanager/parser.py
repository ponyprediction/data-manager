from conf import Conf
from bs4 import BeautifulSoup
import re
from pprint import pprint

class Parser:
	@staticmethod
	def getReunions(date):
		path = Conf.DAY_HTML.replace('DATE',date.strftime('%Y-%m-%d'))
		f = open(path, 'r')
		html = f.read()
		f.close()
		soup = BeautifulSoup(html, "lxml")
		table = soup.find("table", "simple")
		links = table.find_all('a', 'halfpill')
		reunions = []
		for a in links:
			localId = int(a.getText().replace('R', ''))
			globalId = int(re.search(r'\d+', a['href']).group())
			reunions.append({'localId':localId, 'globalId':globalId})
		return reunions

	@staticmethod	
	def getRaces(date, reunion):
		path = Conf.REUNION_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion))
		f = open(path, 'r')
		html = f.read()
		f.close()
		soup = BeautifulSoup(html, "lxml")
		table = soup.find("table", "double")
		links = table.find_all('a', 'pill')
		races = []
		for a in links:
			rx = re.compile(" C(.[0-9]*)")
			localId = int(rx.search(a.getText()).group(1))
			globalId = int(re.search(r'\d+', a['href']).group())
			races.append({'localId':localId, 'globalId':globalId})
		return races

	@staticmethod	
	def getHorsesStart(date, reunion, race):
		raceId = date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(race)
		path = Conf.START_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(race))
		f = open(path, 'r')
		html = f.read()
		f.close()
		soup = BeautifulSoup(html, "lxml")
		table = soup.find_all('table', 'excel')[0]
		lines = table.find_all('tr')
		horses1 = []
		for line in lines:
			cells = line.find_all('td')
			if len(cells) >= 2 and cells[0].getText().strip():
				id = int(re.search(r'\d+', cells[0].getText()).group())
				name = Parser.getCleanHorse(cells[1].getText())
				gender = cells[1].getText()
				gender = re.search(r'\(([^\)]*)\)', gender).group(1)[0]
				age = Parser.getAge(cells[1].getText())
				horses1.append({'id': id, 'name': name, 'gender': gender, 'age': age})
		path = Conf.ODDS_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(race))
		f = open(path, 'r')
		html = f.read()
		f.close()
		soup = BeautifulSoup(html, "lxml")
		table = soup.find_all('table', 'excel')[0]
		lines = table.find_all('tr')
		horses2 = []
		for line in lines:
			cells = line.find_all('td')
			if len(cells) >= 2 and cells[0].getText().strip() :
				id = int(re.search(r'\d+', cells[0].getText()).group())
				name = Parser.getCleanHorse(cells[1].getText())
				gender = cells[1].getText()
				gender = re.search(r'\(([^\)]*)\)', gender).group(1)[0]
				age = Parser.getAge(cells[1].getText())
				horses2.append({'id': id, 'name': name, 'gender': gender, 'age': age})
		if horses1 == horses2:
			return horses2
		else:
			pprint(horses1)
			pprint(horses2)
			raise NameError(raceId + ' : differente horses between start and odds : ' + str(len(horses1)) + ' vs ' + str(len(horses2)))
	
	@staticmethod
	def getHorsesChoice(date, reunion, race):
		raceId = date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(race)
		path = Conf.START_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(race))
		f = open(path, 'r')
		html = f.read()
		f.close()
		soup = BeautifulSoup(html, "lxml")
		table = soup.find_all('table', 'excel')[1]
		lines = table.find_all('tr')
		horses1 = []
		for line in lines:
			cells = line.find_all('td')
			if len(cells) >= 2:
				place = cells[0].getText()
				place = int(re.search(r'\d+', place).group(0))
				id = cells[1].getText()
				id = int(re.search(r'\d+', id).group(0))
				name = cells[1].getText()
				name = re.sub(r'\d+', '', name)
				name = re.sub(r'-', '', name)
				name = name.strip()
				horses1.append({'place': place, 'id': id, 'name': name})
		raceId = date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(race)
		path = Conf.ODDS_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(race))
		f = open(path, 'r')
		html = f.read()
		f.close()
		soup = BeautifulSoup(html, "lxml")
		table = soup.find_all('table', 'excel')[1]
		lines = table.find_all('tr')
		horses2 = []
		for line in lines:
			cells = line.find_all('td')
			if len(cells) >= 2:
				place = cells[0].getText()
				place = int(re.search(r'\d+', place).group(0))
				id = cells[1].getText()
				id = int(re.search(r'\d+', id).group(0))
				name = cells[1].getText()
				name = re.sub(r'\d+', '', name)
				name = re.sub(r'-', '', name)
				name = name.strip()
				horses2.append({'place': place, 'id': id, 'name': name})
		if horses1 == horses2:
			return horses2
		else:
			pprint(horses1)
			pprint(horses2)
			raise NameError(raceId + ' : differente horses between start and odds : ' + str(len(horses1)) + ' vs ' + str(len(horses2)))
		
	@staticmethod	
	def getJockeysStart(date, reunion, race):
		raceId = date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(race)
		path = Conf.START_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(race))
		f = open(path, 'r')
		html = f.read()
		f.close()
		soup = BeautifulSoup(html, "lxml")
		table = soup.find_all('table', 'excel')[0]
		lines = table.find_all('tr')
		jockeys = []
		for line in lines:
			cells = line.find_all('td')
			if len(cells) >= 2 and cells[0].getText().strip():
				id = int(re.search(r'\d+', cells[0].getText()).group())
				name = cells[2].getText()
				name = name.strip()
				jockeys.append({'id': id, 'name': name})
		return jockeys
	
	@staticmethod	
	def getTrainersStart(date, reunion, race):
		raceId = date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(race)
		path = Conf.START_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(race))
		f = open(path, 'r')
		html = f.read()
		f.close()
		soup = BeautifulSoup(html, "lxml")
		table = soup.find_all('table', 'excel')[0]
		lines = table.find_all('tr')
		array = []
		for line in lines:
			cells = line.find_all('td')
			if len(cells) >= 2 and cells[0].getText().strip():
				id = int(re.search(r'\d+', cells[0].getText()).group())
				name = cells[4].getText()
				name = name.strip()
				array.append({'id': id, 'name': name})
		return array
	
	@staticmethod	
	def getOdds(date, reunion, race):
		raceId = date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(race)
		path = Conf.START_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(race))
		f = open(path, 'r')
		html = f.read()
		f.close()
		soup = BeautifulSoup(html, "lxml")
		table = soup.find_all('table', 'excel')[0]
		lines = table.find_all('tr')
		array = []
		for line in lines:
			cells = line.find_all('td')
			if len(cells) >= 2 and cells[0].getText().strip():
				id = int(re.search(r'\d+', cells[0].getText()).group())
				odds1 = cells[5].getText().strip()
				odds1 = float(odds1 if odds1 else 0)
				odds2 = cells[6].getText().strip()
				odds2 = float(odds2 if odds2 else 0)
				odds3 = cells[7].getText().strip()
				odds3 = float(odds3 if odds3 else 0)
				array.append({'id': id, 'odds1': odds1, 'odds2': odds2, 'odds3': odds3})
		return array
		
	@staticmethod
	def getArrival(date, reunion, race):
		raceId = date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(race)
		path = Conf.ARRIVAL_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(race))
		f = open(path, 'r')
		html = f.read()
		f.close()
		soup = BeautifulSoup(html, "lxml")
		table = soup.find_all('table', 'excel')[0]
		lines = table.find_all('tr')
		array = []
		for line in lines:
			cells = line.find_all('td')
			if len(cells) >= 2 and cells[0].getText().strip():
				id = int(re.search(r'\d+', cells[1].getText()).group())
				place = int(re.search(r'\d+', cells[0].getText()).group())
				horse = Parser.getCleanHorse(cells[2].getText())
				array.append({'id': id, 'place': place, 'horse':horse})
		return array
	
	@staticmethod
	def getAge(age):
		age = re.search(r'\((./\d+)\)', age).group(1)
		age = int(re.search(r'\d+', age).group(0))
		return age
	
	@staticmethod
	def getCleanHorse(horse):
		horse = re.sub(r'\([^\)]*\)', '', horse)
		horse = re.sub(r'(E[0-9])', '', horse)
		horse = re.sub(r'\d+', '', horse)
		horse = re.sub(r'-', '', horse)
		horse = horse.strip()
		return horse
		
	@staticmethod
	def getRaceData(date, reunion, race):
		horsesStart = Parser.getHorsesStart(date, reunion, race)
		horsesChoice = Parser.getHorsesChoice(date, reunion, race)
		jockeysStart = Parser.getJockeysStart(date, reunion, race)
		trainersStart = Parser.getTrainersStart(date, reunion, race)
		odds = Parser.getOdds(date, reunion, race)
		arrival = Parser.getArrival(date, reunion, race)
		array = []
		for i, value in enumerate(horsesStart):
			id = horsesStart[i]['id']
			horse = horsesStart[i]['name']
			prediction = None
			place = None
			for x in horsesChoice:
				if x['id'] == id:
					prediction = x['place']
					break
			for x in arrival:
				if x['id'] == id and x['horse'] == horse:
					place = x['place']
					break
			array.append({'id':id, 
				'prediction':prediction, 
				'horse':horse, 
				'gender':horsesStart[i]['gender'], 
				'age':horsesStart[i]['age'],
				'jockey':jockeysStart[i]['name'],
				'trainer':trainersStart[i]['name'],
				'odds1':odds[i]['odds1'],
				'odds2':odds[i]['odds2'],
				'odds3':odds[i]['odds3'],
				'place':place
			})
		return array
		
	
	
	
	
	
	
	
	
	
	
	
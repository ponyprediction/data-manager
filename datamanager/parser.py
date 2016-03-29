from conf import Conf
from bs4 import BeautifulSoup
import re

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
				name = cells[1].getText()
				name = re.sub(r'\([^\)]*\)', '', name)
				name = name.strip()
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
				name = cells[1].getText()
				name = re.sub(r'\([^\)]*\)', '', name)
				name = name.strip()
				gender = cells[1].getText()
				gender = re.search(r'\(([^\)]*)\)', gender).group(1)[0]
				age = Parser.getAge(cells[1].getText())
				horses2.append({'id': id, 'name': name, 'gender': gender, 'age': age})
		if horses1 == horses2:
			return horses2
		else:
			return 'Error : ' + raceId + ' : differente horses between start and odds'
	
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
			return 'Error : ' + raceId + ' : differente horses between start and odds'
		
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
				odds1 = cells[5].getText()
				odds1 = float(odds1.strip())
				odds2 = cells[6].getText()
				odds2 = float(odds2.strip())
				array.append({'id': id, 'odds1': odds1, 'odds2': odds2})
		return array
	
	@staticmethod
	def getAge(age):
		age = re.search(r'\((./\d+)\)', age).group(1)
		age = int(re.search(r'\d+', age).group(0))
		return age
		
	
	
	
	
	
	
	
	
	
	
	

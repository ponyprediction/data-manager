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
	def getHorses(date, reunion, race):
		path = Conf.START_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(race))
		f = open(path, 'r')
		html = f.read()
		f.close()
		soup = BeautifulSoup(html, "lxml")

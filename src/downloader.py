from conf import Conf
from parser import Parser
import datetime
import urllib2
import re
import os
import sys

class Downloader:
	def __init__(self, start, end, force = False):
		self.start = datetime.datetime.strptime(start, '%Y-%m-%d').date()
		self.end = datetime.datetime.strptime(end, '%Y-%m-%d').date()
		self.force = force
		
	def download(self):
		print 'Download from ' + self.start.strftime('%Y-%m-%d') + ' to ' + self.end.strftime('%Y-%m-%d')
		date = self.start	
		day = datetime.timedelta(days=1)
		while date <= self.end:
			self.downloadDay(date)
			reunions = Parser.getReunions(date)
			for reunion in reunions:
				self.downloadReunion(date, reunion['localId'], reunion['globalId'])
				races = Parser.getRaces(date, reunion['localId'])
				for race in races:
					self.downloadRace(date, reunion['localId'], race['localId'], race['globalId'])
			date = date + day
		self.overwrite('')
		print '\rDone'
			
	def downloadDay(self, date):
		self.overwrite(date.strftime('%Y-%m-%d'))
		url = Conf.DAY_URL.replace('DATE',date.strftime('%Y-%m-%d'))
		path = Conf.DAY_HTML.replace('DATE',date.strftime('%Y-%m-%d'))
		self.downloadHtml(url, path)
			
	def downloadReunion(self, date, localId, globalId):
		self.overwrite(date.strftime('%Y-%m-%d') + '-' + str(localId))
		url = Conf.REUNION_URL.replace('ID',str(globalId))
		path = Conf.REUNION_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(localId))
		self.downloadHtml(url, path)
	
	def downloadRace(self, date, reunion, localId, globalId):
		self.overwrite(date.strftime('%Y-%m-%d') + '-' + str(reunion) + '-' + str(localId))
		self.downloadStart(date, reunion, localId, globalId)
		self.downloadOdds(date, reunion, localId, globalId)
		self.downloadArrival(date, reunion, localId, globalId)
		
	def downloadStart(self, date, reunion, localId, globalId):
		url = Conf.START_URL.replace('ID',str(globalId))
		path = Conf.START_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(localId))
		self.downloadHtml(url, path)
		
	def downloadOdds(self, date, reunion, localId, globalId):
		url = Conf.ODDS_URL.replace('ID',str(globalId))
		path = Conf.ODDS_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(localId))
		self.downloadHtml(url, path)
		
	def downloadArrival(self, date, reunion, localId, globalId):
		url = Conf.ARRIVAL_URL.replace('ID',str(globalId))
		path = Conf.ARRIVAL_HTML.replace('DATE',date.strftime('%Y-%m-%d')).replace('REUNION_ID',str(reunion)).replace('RACE_ID',str(localId))
		self.downloadHtml(url, path)
	
	def getHtml(self, url):
		response = urllib2.urlopen(url)
		html = response.read()
		return html
	
	def downloadHtml(self, url, path):
		if not os.path.isfile(path) or self.force:
			html = self.getHtml(url)
			f = open(path, 'w')
			f.seek(0)
			f.write(html)
			f.close()
			
	def overwrite(self, m):
		sys.stdout.write('\r')
		for x in range(0, 80):
			sys.stdout.write(' ')
		sys.stdout.write('\r' + m)
		sys.stdout.flush()


from datamanager.downloader import Downloader
from datamanager.inserter import Inserter
from datamanager.trainer import Trainer
import sys

if len(sys.argv) == 6:
	if sys.argv[1] == 'download': 
		start = sys.argv[3]
		end = sys.argv[5]
		Downloader(start, end).download()
	if sys.argv[1] == 'insert': 
		start = sys.argv[3]
		end = sys.argv[5]
		Inserter(start, end).insert()
	if sys.argv[1] == 'get-training-data': 
		start = sys.argv[3]
		end = sys.argv[5]
		Trainer().get(start, end)

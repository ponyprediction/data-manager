from datamanager.downloader import Downloader
from datamanager.inserter import Inserter
from datamanager.datasetpreparator import DatasetPreparator
from datamanager.tensorflower import TensorFlower
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
		DatasetPreparator().saveTrainingSet(start, end)
	if sys.argv[1] == 'train-show': 
		start = sys.argv[3]
		end = sys.argv[5]
		TensorFlower(start, end).trainShow()
	if sys.argv[1] == 'train-win': 
		start = sys.argv[3]
		end = sys.argv[5]
		TensorFlower(start, end).trainWin()


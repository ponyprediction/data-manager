from downloader import Downloader
import sys

if len(sys.argv) == 6:
	if sys.argv[1] == 'download': 
		start = sys.argv[3]
		end = sys.argv[5]
		Downloader(start, end).download()


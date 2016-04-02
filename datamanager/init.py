from datamanager.conf import Conf
import os

directories = []
directories.append(Conf.DATA_PATH)
directories.append(Conf.HTML_PATH)
directories.append(Conf.HTML_DAYS_PATH)
directories.append(Conf.HTML_REUNIONS_PATH)
directories.append(Conf.HTML_STARTS_PATH)
directories.append(Conf.HTML_ODDS_PATH)
directories.append(Conf.HTML_ARRIVALS_PATH)

for directory in directories:
	if not os.path.exists(directory):
		os.makedirs(directory)
		print(directory)


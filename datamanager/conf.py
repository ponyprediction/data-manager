class Conf:
	ROOT_DIRECTORY = '/home/user/';
	DATA_PATH = ROOT_DIRECTORY + 'data/';
	HTML_PATH = DATA_PATH + 'html/';
	HTML_DAYS_PATH = DATA_PATH + 'html/days/';
	HTML_REUNIONS_PATH = DATA_PATH + 'html/reunions/';
	HTML_STARTS_PATH = DATA_PATH + 'html/starts/';
	HTML_ODDS_PATH = DATA_PATH + 'html/odds/';
	HTML_ARRIVALS_PATH = DATA_PATH + 'html/arrivals/';

	DAY_URL = "http://www.zeturf.fr/fr/resultats-et-rapports/?day=DATE";
	REUNION_URL = "http://www.zeturf.fr/fr/resultats-et-rapports/reunion?id=ID";
	START_URL = "http://www.zeturf.fr/fr/programmes-et-pronostics/course?id=ID";
	ODDS_URL = "http://www.zeturf.fr/fr/les-cotes-zeturf/course?id=ID";
	ARRIVAL_URL = "http://www.zeturf.fr/fr/resultats-et-rapports/course?id=ID";

	DAY_HTML = HTML_DAYS_PATH + "DATE.html";
	REUNION_HTML =  HTML_REUNIONS_PATH + "DATE-REUNION_ID.html";
	START_HTML =  HTML_STARTS_PATH + "DATE-REUNION_ID-RACE_ID-S.html";
	ODDS_HTML =  HTML_ODDS_PATH + "DATE-REUNION_ID-RACE_ID-O.html";
	ARRIVAL_HTML =  HTML_ARRIVALS_PATH + "DATE-REUNION_ID-RACE_ID-A.html";

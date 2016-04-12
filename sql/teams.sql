DROP TABLE IF EXISTS `teams`;
CREATE TABLE IF NOT EXISTS `teams` (
	`id` int not null auto_increment,
	
	`raceId` varchar(255) not null,
	`horseId` int not null,
	`jockeyId` int not null,
	`trainerId` int not null,
	
	`start` int not null,
	`prediction` int not null,
	`arrival` int not null,
	
	`odds1` double not null,
	`odds2` double not null,
	`odds3` double not null,
	
	`firstMoney` double not null,
	`secondMoney` double not null,
	`fourthMoney` double not null,
	`showMoney` double not null,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;

create unique index ids_index on `teams` (raceId, horseId, jockeyId, trainerId);


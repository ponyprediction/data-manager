DROP TABLE IF EXISTS `teamsInRaces`;
CREATE TABLE IF NOT EXISTS `teamsInRaces` (
	`id` int NOT NULL AUTO_INCREMENT,
	`team` int NOT NULL,
	`race` int NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


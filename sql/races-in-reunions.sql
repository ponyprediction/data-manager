DROP TABLE IF EXISTS `racesInReunions`;
CREATE TABLE IF NOT EXISTS `racesInReunions` (
	`id` int NOT NULL AUTO_INCREMENT,
	`race` int NOT NULL,
	`reunion` int NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


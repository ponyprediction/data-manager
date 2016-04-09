DROP TABLE IF EXISTS `reunionsInDays`;
CREATE TABLE IF NOT EXISTS `reunionsInDays` (
	`id` int NOT NULL AUTO_INCREMENT,
	`reunion` int NOT NULL,
	`day` int NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


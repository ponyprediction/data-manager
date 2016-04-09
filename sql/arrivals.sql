DROP TABLE IF EXISTS `arrivals`;
CREATE TABLE IF NOT EXISTS `arrivals` (
	`id` int NOT NULL AUTO_INCREMENT,
	`place` varchar(255) NOT NULL,
	`win` tinyint(1) NOT NULL,
	`winMoney` DOUBLE NOT NULL,
	`placed` tinyint(1) NOT NULL,
	`placedMoney` DOUBLE NOT NULL,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


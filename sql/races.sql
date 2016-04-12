DROP TABLE IF EXISTS `races`;
CREATE TABLE IF NOT EXISTS `races` (
	`id` int(11) not null AUTO_INCREMENT,
	`textId` varchar(255) not null,
	`date` date not null,
	`teamCount` int not null,
	`length` int not null,
	`type` varchar(255) not null,
	PRIMARY KEY (id)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


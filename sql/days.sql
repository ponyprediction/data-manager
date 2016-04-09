DROP TABLE IF EXISTS `days`;
CREATE TABLE IF NOT EXISTS `days` (
	`date` date NOT NULL,
	`reunionCount` int not null,
	PRIMARY KEY (date)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;


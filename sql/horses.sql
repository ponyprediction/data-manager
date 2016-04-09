drop table if exists `horses`;
create table if not exists `horses` (
	`id` int(11) not null auto_increment,
	`name` varchar(255) collate utf8_unicode_ci not null,
	`gender` char(1) collate utf8_unicode_ci not null,
	primary key (id)
) engine=InnoDB default charset=utf8 collate=utf8_unicode_ci;


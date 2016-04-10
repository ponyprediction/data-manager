drop table if exists `trainers`;
create table if not exists `trainers` (
	`id` int(11) not null auto_increment,
	`name` varchar(255) collate utf8_unicode_ci not null unique,
	primary key (id)
) engine=InnoDB default charset=utf8 collate=utf8_unicode_ci;


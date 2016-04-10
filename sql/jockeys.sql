drop table if exists `jockeys`;
create table if not exists `jockeys` (
	`id` int(11) not null auto_increment,
	`name` varchar(255) collate utf8_unicode_ci not null unique,
	primary key (id)
) engine=InnoDB default charset=utf8 collate=utf8_unicode_ci;


use crm;
create table employee(
	employee_Id int primary key auto_increment,
	employee_name varchar(10) not null,
	phone varchar(10) unique not null,
	auth tinyint not null default 1,
	department varchar(10),
	employee_position varchar(10),
	thestatus varchar(10),
	remarks varchar(10),
	__insert_time timestamp not null default current_timestamp,
	__update_time timestamp not null on update current_timestamp default current_timestamp
	);
create table customer(
	customer_Id int primary key auto_increment,
	customer_name varchar(10) not null,
	phone varchar(10) unique not null,
	company varchar(10),
	address varchar(10),
	qq varchar(10),
	wechar varchar(10),
	thestatus varchar(10),
	remarks varchar(10),
	__employee_Id int not null,
	__insert_time timestamp not null default current_timestamp,
	__update_time timestamp not null on update current_timestamp default current_timestamp
	);
create table product(
	product_Id int primary key auto_increment,
	product_name varchar(10) not null,
	model varchar(10) not null,
	num int not null,
	price int not null,
	remarks varchar(10),
	__insert_time timestamp not null default current_timestamp,
	__update_time timestamp not null on update current_timestamp default current_timestamp
	);
create table orderlist(
	id int primary key auto_increment,
	order_Id int not null,
	order_key varchar(10) not null,
	order_value varchar(10) not null,
	key_num int not null,
	remarks varchar(10),
	__insert_time timestamp not null default current_timestamp,
	__update_time timestamp not null on update current_timestamp default current_timestamp
	);
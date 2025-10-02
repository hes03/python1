-- SQLite
select * from juso;

create table product(
    code integer PRIMARY KEY AUTOINCREMENT, 
    name char(100), 
    price integer DEFAULT 0
);

SELECT * from product;
INSERT into product(name, price)
values('LG 세탁기', 2500000);
INSERT into product(name, price)
values('LG 냉장고', 3500000);

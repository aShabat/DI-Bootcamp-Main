/*
    Create a database called public.
    Add two tables:
        items
        customers.


Follow the instructions below to determine which columns and data types to add to the two tables:

    Add the following items to the items table:
        1 - Small Desk – 100 (ie. price)
        2 - Large desk – 300
        3 - Fan – 80

    Add 5 new customers to the customers table:
        1 - Greg - Jones
        2 - Sandra - Jones
        3 - Scott - Scott
        4 - Trevor - Green
        5 - Melanie - Johnson

    Use SQL to fetch the following data from the database:
        All the items.
        All the items with a price above 80 (80 not included).
        All the items with a price below 300. (300 included)
        All customers whose last name is ‘Smith’ (What will be your outcome?).
        All customers whose last name is ‘Jones’.
        All customers whose firstname is not ‘Scott’.
*/

create table public.items(
	ID serial primary key,
	Name varchar(255),
	Price int
);

create table public.customers(
	ID serial primary key,
	FirstName varchar(255),
	LastName varchar(255)
);

insert into public.items (Name, Price) values
('Small desk', 100), ('Large desk', 300), ('Fan', 80);

insert into public.customers (FirstName, LastName) values
('Greg', 'Jones'), ('Sandra', 'Jones'), ('Scott', 'Scott'), ('Trevor', 'Green'), ('Melanie', 'Johnson');

select * from public.items;

select ID, Name, Price from public.items
where Price > 80;

select ID, Name, Price from public.items
where Price <= 300;

select ID, FirstName, LastName from public.customers
where LastName like 'Smith';

select ID, FirstName, LastName from public.customers
where LastName like 'Jones';

select ID, FirstName, LastName from public.customers
where LastName not like 'Scott';

-- drop table public.items;
-- drop table public.customers;

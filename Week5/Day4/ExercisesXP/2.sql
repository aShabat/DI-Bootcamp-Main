-- We will use the newly installed dvdrental database.
--
--     In the dvdrental database write a query to select all the columns from the “customer” table.
--
--     Write a query to display the names (first_name, last_name) using an alias named “full_name”.
--
--     Lets get all the dates that accounts were created. Write a query to select all the create_date from the “customer” table (there should be no duplicates).
--
--     Write a query to get all the customer details from the customer table, it should be displayed in descending order by their first name.
--
--     Write a query to get the film ID, title, description, year of release and rental rate in ascending order according to their rental rate.
--
--     Write a query to get the address, and the phone number of all customers living in the Texas district, these details can be found in the “address” table.
--
--     Write a query to retrieve all movie details where the movie id is either 15 or 150.
--
--     Write a query which should check if your favorite movie exists in the database. Have your query get the film ID, title, description, length and the rental rate, these details can be found in the “film” table.
--
--     No luck finding your movie? Maybe you made a mistake spelling the name. Write a query to get the film ID, title, description, length and the rental rate of all the movies starting with the two first letters of your favorite movie.
--
--     Write a query which will find the 10 cheapest movies.
--
--     Not satisfied with the results. Write a query which will find the next 10 cheapest movies.
--     Bonus: Try to not use LIMIT.
--
--     Write a query which will join the data in the customer table and the payment table. You want to get the first name and last name from the curstomer table, as well as the amount and the date of every payment made by a customer, ordered by their id (from 1 to…).
--
--     You need to check your inventory. Write a query to get all the movies which are not in inventory.
--
--     Write a query to find which city is in which country.
--
--     Bonus You want to be able to see how your sellers have been doing? Write a query to get the customer’s id, names (first and last), the amount and the date of payment ordered by the id of the staff member who sold them the dvd.

select * from customer;

select first_name || ' ' || last_name as full_name from customer;

select distinct create_date;

select * from customer
order by first_name;

select film_id as ID, title, description, release_year, rental_rate from film
order by rental_rate asc;

select address, phone from address
where district like 'Texas';

select * from film
where film_id in (15, 50);

select * from film
where title like 'Prestige';

select * from film
where title like 'Pr%';

select * from film
order by rental_rate asc
limit 10;

select * from film
order by rental_rate asc
limit 10
offset 10;

select c.first_name, c.last_name, p.amount, p.payment_date from customer c
inner join payment p on p.customer_id = c.customer_id
order by p.payment_id;

select f.title from film f
left join inventory i on f.film_id = i.film_id
where i.inventory_id is null;

select city, country from city
full outer join country on city.country_id = country.country_id;

select c.customer_id, c.first_name, c.last_name, p.amount, p.payment_date from customer c
inner join payment p on p.customer_id = c.customer_id
order by p.staff_id;

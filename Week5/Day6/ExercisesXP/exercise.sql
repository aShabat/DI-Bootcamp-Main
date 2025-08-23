-- 🌟 Exercise 1: DVD Rental
-- Instructions
--
--     Get a list of all the languages, from the language table.
--
--     Get a list of all films joined with their languages – select the following details : film title, description, and language name.
--
--     Get all languages, even if there are no films in those languages – select the following details : film title, description, and language name.
--
--     Create a new table called new_film with the following columns : id, name. Add some new films to the table.
--
--     Create a new table called customer_review, which will contain film reviews that customers will make.
--     Think about the DELETE constraint: if a film is deleted, its review should be automatically deleted.
--     It should have the following columns:
--         review_id – a primary key, non null, auto-increment.
--         film_id – references the new_film table. The film that is being reviewed.
--         language_id – references the language table. What language the review is in.
--         title – the title of the review.
--         score – the rating of the review (1-10).
--         review_text – the text of the review. No limit on the length.
--         last_update – when the review was last updated.
--
--     Add 2 movie reviews. Make sure you link them to valid objects in the other tables.
--
--     Delete a film that has a review from the new_film table, what happens to the customer_review table?
--
--
-- 🌟 Exercise 2 : DVD Rental
-- Instructions
--
--     Use UPDATE to change the language of some films. Make sure that you use valid languages.
--
--     Which foreign keys (references) are defined for the customer table? How does this affect the way in which we INSERT into the customer table?
--
--     We created a new table called customer_review. Drop this table. Is this an easy step, or does it need extra checking?
--
--     Find out how many rentals are still outstanding (ie. have not been returned to the store yet).
--
--     Find the 30 most expensive movies which are outstanding (ie. have not been returned to the store yet)
--
--     Your friend is at the store, and decides to rent a movie. He knows he wants to see 4 movies, but he can’t remember their names. Can you help him find which movies he wants to rent?
--         The 1st film : The film is about a sumo wrestler, and one of the actors is Penelope Monroe.
--
--         The 2nd film : A short documentary (less than 1 hour long), rated “R”.
--
--         The 3rd film : A film that his friend Matthew Mahan rented. He paid over $4.00 for the rental, and he returned it between the 28th of July and the 1st of August, 2005.
--
--         The 4th film : His friend Matthew Mahan watched this film, as well. It had the word “boat” in the title or description, and it looked like it was a very expensive DVD to replace.

select distinct name from language;

select f.title, f.description, l.name from film f
left join language l on f.language_id = l.language_id;

select f.title, f.description, l.name from film f
right join language l on f.language_id = l.language_id;

create table new_film(
    id serial primary key,
    name varchar(255)
);

insert into new_film (name) values
('Wally'), ('Die Hard'), ('Lost in Highway');

create table customer_review (
    review_id serial not null primary key,
    film_id integer references new_film (id) on delete cascade,
    language_id integer references language (language_id) on delete restrict,
    title varchar(255),
    score integer check(score >= 1 and score <= 10),
    review_text text,
    last_update date default current_date
);

insert into customer_review (film_id, language_id, title, score, review_text) values
    ((select id from new_film where name = 'Wally' limit 1), (select language_id from language where name='English'), 'bad', 1, 'i didn''t like it'),
    ((select id from new_film where name = 'Die Hard' limit 1), (select language_id from language where name='English'), 'good', 10, 'good stuff');

delete from new_film
where name = 'Wally';

select * from customer_review;

update new_film
set language_id = (select language_id from language where name='French')
where score=10;

drop table customer_review;

select count(*) from rental
where return_date is null;

select r.* from rental r
left join payment p on r.rental_id = p.rental_id
where return_date is null
order by p.amount desc
limit 30;

select f.title from film f
right join film_actor fa on fa.film_id = f.film_id
left join actor a on fa.actor_id = a.actor_id
where a.first_name = 'Penelope' and a.last_name = 'Monroe'
and f.fulltext @@ to_tsquery('sumo');

select title from film
where length <= 60
and rating = 'R'
and description like '%Documentary%';

select f.title from film f
inner join inventory i on f.film_id = i.film_id
inner join rental r on i.inventory_id = r.inventory_id
inner join payment p on r.rental_id = p.rental_id
inner join  customer c on c.customer_id = r.customer_id
where c.first_name = 'Matthew' and c.last_name = 'Mahan'
and p.amount >= 4
and r.return_date >= '7/28/2005' and r.return_date <= '8/1/2005';

select f.title from film f
inner join inventory i on f.film_id = i.film_id
inner join rental r on i.inventory_id = r.inventory_id
inner join  customer c on c.customer_id = r.customer_id
where c.first_name = 'Matthew' and c.last_name = 'Mahan'
and (f.title ilike '%boat%' or f.description ilike '%boat%')
order by f.replacement_cost desc
limit 1;

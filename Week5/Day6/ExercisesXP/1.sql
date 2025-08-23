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

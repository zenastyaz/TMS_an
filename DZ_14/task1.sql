--Создание и заполнение таблиц
--● Создайте таблицу authors с полями id, first_name и
--last_name. Используйте PRIMARY KEY для поля id
--● Создайте таблицу books с полями id, title, author_id и
--publication_year. Используйте PRIMARY KEY для поля id и
--FOREIGN KEY для поля author_id, ссылаясь на таблицу
--authors
--● Создайте таблицу sales с полями id, book_id и quantity.
--Используйте PRIMARY KEY для поля id и FOREIGN KEY для
--поля book_id, ссылаясь на таблицу books
--● Добавьте несколько авторов в таблицу authors
--● Добавьте несколько книг в таблицу books, указывая
--авторов из таблицы authors
--● Добавьте записи о продажах книг в таблицу sales



create table authors
(
id serial primary key,
first_name text,
last_name text
);

create table books
(
id serial primary key,
title text,
author_id int references authors(id),
publication_year integer
);

create table sales
(
id serial primary key,
book_id int references books(id),
quantity int
);

insert into authors(first_name, last_name) values
('Leo', 'Tolstoy'),
('Fyodor', 'Dostoevsky'),
('Anton', 'Chekhov'),
('Alexander', 'Pushkin'),
('Nikolai', 'Gogol'),
('Ivan', 'Turgenev');

insert into books(title, author_id, publication_year) values
('War and Peace', 1, 1869),
('Anna Karenina', 1, 1877),
('Crime and Punishment', 2, 1866),
('The Idiot', 2, 1869),
('The Cherry Orchard', 3, 1904),
('Eugene Onegin', 4, 1832),
('Dead Souls', 5, 1842),
('Fathers and Sons', 6, 1862);

insert into sales (book_id, quantity) values
(1, 120),
(2, 150),
(3, 90),
(4, 200),
(5, 80),
(6, 170),
(7, 70),
(8, 130);
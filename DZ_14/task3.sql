--Множественные JOIN
--● Используйте INNER JOIN для связывания таблиц authors,
--books и sales, чтобы получить список всех книг, их авторов
--и продаж
--● Используйте LEFT JOIN для связывания таблиц authors,
--books и sales, чтобы получить список всех авторов, их книг
--и продаж (включая авторов без книг и книги без продаж)


select a.first_name, a.last_name, b.title, b.publication_year, s.quantity
from authors a
inner join books b on a.id = b.author_id
inner join sales s on b.id = s.book_id;

select a.first_name, a.last_name, b.title, b.publication_year, s.quantity
from authors a
left join books b on a.id = b.author_id
left join sales s on b.id = s.book_id
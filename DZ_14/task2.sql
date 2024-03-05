--Использование JOIN
--● Используйте INNER JOIN для получения списка всех книг и
--их авторов.
--● Используйте LEFT JOIN для получения списка всех авторов
--и их книг (включая авторов, у которых нет книг).
--● Используйте RIGHT JOIN для получения списка всех книг и
--их авторов, включая книги, у которых автор не указан


select books.title, authors.first_name, authors.last_name
from books
inner join authors on books.author_id = authors.id;

select authors.first_name, authors.last_name, books.title
from authors
left join books on authors.id = books.author_id;

select books.title, authors.first_name, authors.last_name
from books
right join authors on books.author_id = authors.id;

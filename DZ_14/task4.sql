--Агрегация данных с использованием JOIN
--● Используйте INNER JOIN и функции агрегации для
--определения общего количества проданных книг каждого
--автора
--● Используйте LEFT JOIN и функции агрегации для
--определения общего количества проданных книг каждого
--автора, включая авторов без продаж


select a.first_name, a.last_name, sum(s.quantity) as total_sales
from authors a
inner join books b on a.id = b.author_id
inner join sales s on b.id = s.book_id
group by a.first_name, a.last_name;

select a.first_name, a.last_name, sum(s.quantity) as total_sales
from authors a
left join books b on a.id = b.author_id
left join sales s on b.id = s.book_id
group by a.first_name, a.last_name;


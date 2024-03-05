--Подзапросы и JOIN
--● Найдите автора с наибольшим количеством проданных
--книг, используя подзапросы и JOIN
--● Найдите книги, которые были проданы в количестве,
--превышающем среднее количество продаж всех книг,
--используя подзапросы и JOIN


select a.first_name, a.last_name
from authors a
join (
    select b.author_id, sum(s.quantity) as total_sales
    from books b
    join sales s on b.id = s.book_id
    group by b.author_id
    LIMIT 1
) as top_author on a.id = top_author.author_id;

select b.title, a.first_name, a.last_name, s.quantity
from books b
join authors a on b.author_id = a.id
join sales s on b.id = s.book_id
where s.quantity > (select avg(quantity)from sales);

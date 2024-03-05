--Найдите книги, которые были проданы в количестве,
--превышающем среднее количество продаж каждой из книг,
--используя подзапросы и JOIN


select a.first_name, a.last_name, avg(s.quantity) as average_sales
from authors as a
join books as b on b.author_id = a.id
join sales as s on s.book_id = b.id
group by a.first_name, a.last_name
having avg(s.quantity) > (
    select avg(quantity)
    from sales
);

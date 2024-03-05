--Представим, что у нас есть таблица "Employees" с
--полями "Name", "Position", "Department", "Salary".
--● Создайте таблицу "Employees" с указанными полями.
--● Вставьте в таблицу несколько записей с информацией о
--сотрудниках вашей компании.
--● Измените данные в таблице для каких-то сотрудников.
--Например, изменим должность одного из сотрудников на
--более высокую.
--● Добавьте новое поле "HireDate" (дата приема на работу) в
--таблицу "Employees".
--● Добавьте записи о дате приема на работу для всех
--сотрудников.
--● Найдите всех сотрудников, чья должность "Manager".
--● Найдите всех сотрудников, у которых зарплата больше
--5000 долларов.
--● Найдите всех сотрудников, которые работают в отделе
--"Sales".
--● Найдите среднюю зарплату по всем сотрудникам.
--● Удалите таблицу "Employees". DROP TABLE Employees;

create table employees
(
id serial primary key,
Name text,
Position text,
Department text,
Salary integer
);

insert into employees (Name, Position, Department, Salary) VALUES
('Иванов', 'Менеджер', 'Продажи', 1700),
('Сидоров', 'Разработчик', 'IT', 1300),
('Петров', 'Аналитик', 'Маркетинг', 1300),
('Сидорова', 'Разработчик', 'IT', 1600),
('Алексеева', 'Дизайнер', 'Дизайн', 1400);

update employees
set Position = 'Старший менеджер'
where Name = 'Иванов';

alter table employees
add column HireDate date;

update employees
set HireDate = '2023-01-01'
where Name = 'Иванов';

update employees
set HireDate = '2023-01-02'
where Name = 'Сидоров';

update employees
set HireDate = '2023-01-03'
where Name = 'Петров';

update employees
set HireDate = '2023-01-04'
where Name = 'Сидорова';

update employees
set HireDate = '2023-01-05'
where Name = 'Алексеева';

select * from employees
where Position like '%Аналитик%'

select * from employees
where Salary > 1500;

select * from employees
where Department = 'IT';

select avg(Salary) from employees;

drop table employees;
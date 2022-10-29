-- ex6
select * from movies
inner join boxoffice
on movies.id = boxoffice.movie_id;

select * from movies
inner join boxoffice
on movies.id = boxoffice.movie_id
where international_sales > domestic_sales;

select * from movies
inner join boxoffice
on movies.id = boxoffice.movie_id
order by rating desc;

-- ex7
select distinct building_name from buildings
left join employees
on buildings.building_name = employees.building
where role not like 'null';

select distinct building_name, capacity from buildings;

select distinct building_name, role from buildings
left join employees
on buildings.building_name = employees.building;

-- ex8
select name, role from employees
where building is null;

select distinct building_name from buildings
left join employees
on buildings.building_name = employees.building
where name is null;

-- ex9
select title, (domestic_sales + international_sales) / 1000000 as combined_sales
from movies
join boxoffice
on movies.id = boxoffice.movie_id;

select title, rating * 10 as rating_perc
from movies
join boxoffice
on movies.id = boxoffice.movie_id; 

select title, year from movies
where year % 2 = 0;

-- ex10
select max(years_employed) from employees;

select role, avg(years_employed)
from employees
group by role;

select building, sum(years_employed)
from employees
group by building;

-- ex11
select count(role) from employees
where role like 'artist';

select role, count(name)
from employees
group by role;

select sum(years_employed)
from employees
group by role
having role like 'engineer';

-- ex12
select director, count(title) from movies
group by director;

select director, sum(domestic_sales + international_sales) as Total_sales
from movies
join boxoffice
on movies.id = boxoffice.movie_id
group by director;

-- ex13
insert into movies
(title, director, year, length_minutes)
values('Toy Story 4', 'Josh Cooley', 2019, 100);

insert into boxoffice
values(15, 8.7, 340000000, 270000000); 
-- unsure if somehow could pass an id value of 15 from movies table

-- ex14
update movies
set director = 'John Lasseter'
where title = "A Bug's Life";

update movies
set year = 1999
where title = 'Toy Story 2';

-- ex15
delete from movies
where year < 2005; 

delete from movies
where director = "Andrew Stanton";

-- ex16
create table if not exists Database
(Name text, Version float, Download_count int);

-- ex17
alter table movies
add Aspect_ratio float;

alter table movies
add Language text default 'English';

-- ex18
drop table if exists movies;

drop table if exists boxoffice;
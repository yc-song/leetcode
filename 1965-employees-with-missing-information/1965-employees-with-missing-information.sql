(select e.employee_id as employee_id
from Employees e
left outer join Salaries s on (e.employee_id = s.employee_id)
where s.salary is null)
union
(select s2.employee_id as employee_id
from Employees e2
right outer join Salaries s2 on (e2.employee_id = s2.employee_id)
where e2.name is null)
order by employee_id asc
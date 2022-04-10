
select d.name as Department, e1.name as Employee, salary as Salary
from Employee e1
join Department d on (e1.departmentId = d.id)
where e1.salary>=( select min(s) from (select distinct salary as s
from Employee e2   
where e2.departmentId = e1.departmentId
order by salary desc
limit 3 
) as t) 


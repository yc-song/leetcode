/* Write your T-SQL query statement below */
select distinct logs.num as ConsecutiveNums
from logs
left outer join (select id, num 
     from logs
     ) as l2 on (l2.id = logs.id+1)
left outer join (select id, num 
from logs
) as l3 on (l3.id = logs.id+2)
where logs.num = l2.num and l2.num = l3.num



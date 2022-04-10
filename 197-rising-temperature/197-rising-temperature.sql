
select id
from Weather 
left outer join
(select DATEADD(day, 1, recordDate) as new_date, temperature as new_temp
from Weather) as t on (Weather.recordDate = t.new_date)
where new_temp-temperature<0


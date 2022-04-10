select distinct p.product_id, product_name
from Product p
join Sales s on (p.product_id= s.product_id)
where sale_date>='2019-01-01' and sale_date<='2019-03-31' 
except
select p.product_id, product_name
from Product p
join Sales s on (p.product_id= s.product_id)
where (sale_date<'2019-01-01' or sale_date>'2019-03-31')
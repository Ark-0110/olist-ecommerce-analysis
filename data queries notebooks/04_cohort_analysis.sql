with first_order as (
select c.customer_unique_id, Min(o.order_purchase_timestamp) as first_order_date
from orders o
left join customers c on o.customer_id  = c.customer_id
group by c.customer_unique_id)

select * from first_order
limit 10;




with first_order as (
select c.customer_unique_id, Min(o.order_purchase_timestamp) as first_order_date
from orders o
left join customers c on o.customer_id  = c.customer_id
group by c.customer_unique_id),

cohort_orders as (
select c.customer_unique_id, Date_trunc('month',fo.first_order_date) as cohort_month, extract
(year from AGE(o.order_purchase_timestamp, fo.first_order_date)) * 12 + extract(month from 
AGE(o.order_purchase_timestamp, fo.first_order_date)) as month_offset
from orders o
left join customers c on o.customer_id = c.customer_id
left join first_order fo on c.customer_unique_id = fo.customer_unique_id)

select cohort_month, month_offset, count(distinct customer_unique_id) as customers
from cohort_orders
WHERE cohort_month >= '2017-01-01' 
AND cohort_month <= '2018-08-01'
group by cohort_month, month_offset
order by cohort_month, month_offset; 
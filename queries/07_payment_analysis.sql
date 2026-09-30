select op.payment_type, count(distinct o.order_id) as total_orders, sum(op.payment_value) as total_revenue, 
round(avg(op.payment_installments)::numeric,2) as avg_installments, round(avg(op.payment_value)::numeric,2) as avg_order_value
from orders o
left join order_payments op on o.order_id = op.order_id 
where o.order_purchase_timestamp >= '2017-01-01' AND o.order_purchase_timestamp <= '2018-08-31'
AND op.payment_type != 'not_defined'
group by op.payment_type 
order by total_orders;
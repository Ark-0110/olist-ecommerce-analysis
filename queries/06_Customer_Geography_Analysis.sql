select c.customer_state, sum(op.payment_value) as total_revenue, COUNT(DISTINCT o.order_id) as total_orders,
ROUND(AVG(op.payment_value)::numeric, 2) as avg_order_value
from orders o
left join order_payments op on o.order_id = op.order_id
left join customers c on o.customer_id = c.customer_id
where o.order_purchase_timestamp >= '2017-01-01' 
AND o.order_purchase_timestamp <= '2018-08-31'
and o.order_status not in ('cancelled', 'unavailable')
group by c.customer_state 
order by total_revenue desc;
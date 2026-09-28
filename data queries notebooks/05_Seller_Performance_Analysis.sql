select oi.seller_id, count(distinct o.order_id) as total_orders, 
Sum(oi.price) as total_revenue, Avg(r.review_score) as avg_review_score
from orders o
left join order_items oi on o.order_id = oi.order_id
left join order_reviews r on o.order_id = r.order_id
where o.order_status = 'delivered' and o.order_purchase_timestamp >= '2017-01-01' 
AND o.order_purchase_timestamp <= '2018-08-31'
group by oi.seller_id
having count(distinct o.order_id) > 30
order by avg_review_score asc;
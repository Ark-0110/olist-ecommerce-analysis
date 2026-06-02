SELECT oi.seller_id, ROUND(AVG(extract(DAY FROM(o.order_delivered_customer_date - o.order_purchase_timestamp)))) 
as actualavg, ROUND(AVG(extract(DAY FROM(o.order_estimated_delivery_date - o.order_purchase_timestamp))))
as estimatedavg, ROUND(AVG(EXTRACT(DAY FROM (o.order_delivered_customer_date - o.order_purchase_timestamp))) 
- AVG(EXTRACT(DAY FROM (o.order_estimated_delivery_date - o.order_purchase_timestamp))))
as difference, COUNT(DISTINCT o.order_id) as sellerstotal
FROM orders o
LEFT JOIN order_items oi ON o.order_id = oi.order_id
where order_status = 'delivered' and (o.order_purchase_timestamp >= '2017-01-01' and 
o.order_purchase_timestamp <= '2018-08-31') 
group by oi.seller_id
having COUNT(DISTINCT o.order_id) > 30
order by difference desc;
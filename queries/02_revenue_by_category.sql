SELECT ct.product_category_name_english, SUM(oi.price) as  TotalRevenueperCategory, 
COUNT(DISTINCT o.order_id) as TotalOrdersperCategory, AVG(oi.price) as AVGitemperPrice
FROM orders o
LEFT JOIN order_items oi ON o.order_id = oi.order_id
LEFT JOIN products p ON oi.product_id = p.product_id
LEFT JOIN category_translation ct ON p.product_category_name = ct.product_category_name
WHERE o.order_status NOT IN ('cancelled', 'unavailable') and  (o.order_purchase_timestamp >= '2017-01-01' and o.order_purchase_timestamp <= '2018-08-31') 
group by ct.product_category_name_english 
order by 2 DESC;
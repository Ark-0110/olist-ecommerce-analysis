SELECT 
    DATE_TRUNC('month', o.order_purchase_timestamp) AS month,
    ROUND(SUM(p.payment_value)::numeric, 2) AS total_revenue,
    COUNT(DISTINCT o.order_id) AS total_orders,
    ROUND(AVG(p.payment_value)::numeric, 2) AS avg_order_value
FROM orders o
LEFT JOIN order_payments p ON o.order_id = p.order_id
WHERE o.order_status NOT IN ('cancelled', 'unavailable') and  (order_purchase_timestamp > '2017-01-01' and order_purchase_timestamp < '2018-08-31') 
GROUP BY 1
ORDER BY 1;
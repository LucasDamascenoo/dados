
-- receita media gerada por cliente

SELECT
t2.customer_state,
ROUND(sum(t3.price) / COUNT(DISTINCT t1.customer_id),2) as avg_receita_cliente
FROM tb_orders as t1
left join tb_customers as t2
on t1.customer_id = t2.customer_id
left join tb_order_items as t3
on t1.order_id = t3.order_id
where t1.order_status = 'delivered'
GROUP BY t2.customer_state
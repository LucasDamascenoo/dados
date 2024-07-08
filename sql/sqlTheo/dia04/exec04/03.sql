
-- qual o peso medio dos produtos vendidos por sellers por cada estado
-- apenas ano de 2017 e pedidos entregues



select
t4.seller_state,
round(AVG(t3.product_weight_g),2) as media_produto
from tb_orders as t1
LEFT JOIN tb_order_items as t2
ON t1.order_id = t2.order_id
LEFT JOIN tb_products as t3
on t2.product_id = t3.product_id
LEFT JOIN tb_sellers as t4
ON t2.seller_id =  t4.seller_id
where t1.order_status = 'delivered'
and strftime("%Y",order_approved_at) = '2017'
GROUP BY t4.seller_state
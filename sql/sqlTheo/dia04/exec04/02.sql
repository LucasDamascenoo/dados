
-- TOTAL DE RECEITA POR SELLERS

select
 t3.seller_state,
 round(sum(t2.price),2) receita_total,
 round(sum(t2.price)/ count(DISTINCT t2.seller_id),2 ) as media_sellers,
 count(DISTINCT t2.seller_id) as qtd_sellers
from tb_orders as t1
LEFT JOIN tb_order_items as t2
ON t1.order_id = t2.order_id
LEFT JOIN tb_sellers as t3
ON t2.seller_id = t3.seller_id
where t1.order_status = "delivered"
GROUP BY t3.seller_state
ORDER BY receita_total DESC
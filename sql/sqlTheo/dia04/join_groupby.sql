-- qual a receita de cada categoria de produto 
-- e o total de vendas?
-- em unidades e em pedidos?


SELECT 
t2.product_category_name,
round(sum(t1.price),2) as Receita,
count(*) as qtd_vendidas,
count(DISTINCT t1.order_id) as qtd_itens_pedidos,
round(count(*) / cast(count(DISTINCT t1.order_id) as float),2) as avg_item_por_pedido
FROM tb_order_items as t1
left join tb_products as t2
on t1.product_id = t2.product_id
GROUP BY t2.product_category_name
order by round(sum(t1.price),2) DESC
limit 10;
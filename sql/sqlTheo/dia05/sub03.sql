
with tb_best_category as (

select t2.product_category_name
from tb_order_items as t1
left join tb_products as t2
on t1.product_id = t2.product_id
group by t2.product_category_name
order by coun(*) desc
limit 3
), as

SELECT
 t2.seller_state,
 t1.product_id,
 t3.product_category_name,
 sum(t1.price) as receita_total
From tb_order_items as t1

left join tb_sellers as t2
on t1.seller_id = t2.seller_id
left join tb_products as t3
on t1.product_id = t3.product_id
inner join tb_best_category  as bc
on t3.product_category_name = bc.product_category_name
group by 
t2.seller_state,
 t1.product_id,
 t3.product_category_name

 -- with


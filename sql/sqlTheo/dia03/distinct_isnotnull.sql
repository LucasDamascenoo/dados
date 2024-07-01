
SELECT DISTINCT 
CASE
WHEN product_category_name IS NULL THEN 'OUTROS'
ELSE product_category_name END AS categoria_fillna
FROM tb_products;
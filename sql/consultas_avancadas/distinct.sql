
-- utilizamos o distinct para trazer apenas dados distintos (diferentes)



USE SUCO_VENDAS

SELECT DISTINCT
 EMBALAGEM,
 SABOR 
 FROM TABELA_DE_PRODUTOS
WHERE SABOR = 'Maca'
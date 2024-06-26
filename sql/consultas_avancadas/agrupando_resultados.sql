
-- Podemos agrupar os resultados 
-- precisa ter pelo menos um agrupamento (sum-avg-max-min)
--




USE SUCO_VENDAS

SELECT  CIDADE,IDADE
 FROM TABELA_DE_CLIENTES


-- GRUOUP BY

SELECT
 CIDADE,
 AVG(IDADE) AS MEDIA_IDADE
 FROM TABELA_DE_CLIENTES
 GROUP BY CIDADE


 -- HAVING
-- Utilizado para "filtrar" agregações


SELECT
 ESTADO,
 SUM(LIMITE_DE_CREDITO) AS LIMITE
 FROM TABELA_DE_CLIENTES
 GROUP BY ESTADO
 HAVING SUM(LIMITE_DE_CREDITO) >= 900000
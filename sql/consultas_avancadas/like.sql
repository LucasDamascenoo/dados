 -- utilizado para filtrar uma determinada parte de um texto

 USE SUCO_VENDAS


 -- '%Teste'
 -- começa com qualquer caracter e termina com teste

 -- Exemplo 'Area de Teste'


 SELECT * FROM TABELA_DE_PRODUTOS
 WHERE SABOR LIKE '%Limao'
 -- Lima/Limao - Morango/Limao

 -- 'Teste%'
 -- começa com o texto do filtro e termina com qualquer caracter

 -- Exemplo 'Teste da Jessica'

 SELECT * FROM TABELA_DE_PRODUTOS
 WHERE SABOR LIKE 'Morango%'




-- '%TESTE%'
-- Começa com qualquer caracter, tem o Teste no meio e termina com qualquer caracter

-- Exemplo ' Sala de Teste de Mátematica'

 SELECT * FROM TABELA_DE_CLIENTES
 WHERE NOME LIKE '%Silva%'
# SQL - Sequel

Documentando meus estudos e projetos em SQL.

## Conceitos

### Normalização

Normalizamos tabela para que os dados sejam lidos e gravados de forma mais clara, ao invez de termos um unico tabelão de vendas, podemos dividir em diversas tabela, como produtos, vendedores, vendas, cliente.

### Chave Primaria e Chave Estrangeira

- Chave Primaria: Chave primaria identificar um registro unico em uma tabela (ID,CPF,NSU)
- Chave Estrangeira: Chave primaria de uma tabela que foi adicionado em outra tabela.

### Consultas (Querys)

O objetivo das consultas é retornar dados de uma determinada tabela/view, para isso usamos o SELECT.

- Selecionando todas as colunas

```sql 
select *
from needful_things.orders

```
- Selecionando colunas especificas
```sql 
select 
  category, products
from needful_things.orders

```

### Order By
Responsavel por ordernar uma ou mais colunas

```sql 
select 
*
from needful_things.orders
order by salario -- vai order o resultado pelos salarios (menor para o maior)
order by salario DESC -- orderna do maior para o menor
```
**Em casos númericos sempre vai ser do maior para o menor ou do menor para o maior**
**Em casos de textos, vai respeitar a ordem alfabetica**

```sql 
select 
nome,
idade,
sexo
from needful_things.orders
order by 1 -- vai ordernar pela primeiro campo do select ( no caso o nome)

```

### Group By

Group by é responsavel por agrupar campos que possuem agregações(min,max...)

**Não podemos selecionar o campo de que está fazendo a operação de agregação**

```sql 
SELECT
CIDADE,
COUNT(ID_FUNC) AS QTD_FUNCIONARIO
FROM FUNCIONARIOS
GROUP BY CIDADE
```

### Where vs Having

- Where é usado para filtrar colunas(aritmeticas e demais) de forma individual
**Não podemos usar funções de agregações em um where, isso se da por conta da ordem de execução do sql (where vem antes do groupby)**

- Having somente é usando com as operações de uma agregação (min,max...)

```sql 
SELECT
CIDADE,
COUNT(ID_FUNC) AS QTD_FUNCIONARIO
FROM FUNCIONARIOS
GROUP BY CIDADE
HAVING COUNT(ID_FUNC) > 1 -- NESSES EXEMPLOS PODEMOS VERIFICAR SE EXISTE DUPLICIDADE DE IDS
```

**Podemos combinar Where com Having**

```sql 
SELECT
NUMERO,
QUANTIDADE,
ROUND(SUM(PRECO),2) AS PRECO
FROM [dbo].[ITENS_NOTAS_FISCAIS]
WHERE CODIGO_DO_PRODUTO IN (723457,1078680,290478,1004327)
GROUP BY
NUMERO,
QUANTIDADE
HAVING SUM(PRECO) > 2
```

### Distinc

retorna valores distintos de uma determinada coluna.

```sql 
SELECT DISTINCT * FROM tb_products;
```
### top

Limita a quantidade de registros em uma consulta SQL.

```sql 
select 
 top 10 *
from needful_things.orders


```


### Aliases

Podemos criar 'apelidos' tanto em colunas quanto em tabelas utilizando o AS

```sql 
select 
  category AS categoria,
  products AS produtos
from needful_things.orders
where products in ('pa','ra','dh') and values >= 1000 -- vai retornar dados apenas se todas as condições forem verdade

select 
  category, products
from needful_things.orders AS order
where products  in ('pa','ra','dh') or cidade in ('sp','rj','ba') -- vai retornar dados apenas se uma das condições forem verdade
```

### Ordem de execução

Essa é a ordem de execução em uma query sql.

1º FROM 
2º WHERE 
3º GROUP BY
4º HAVING
5º SELECT
6º ORDER BY
7º TOP



## Filtros

Quando trabalhamos com consultas, nem sempre vamos querer retornar tudo, as vezes queremos retornar dados atráves de uma determinada condição, em conjunto com o where temos 5 tipos de condicoes que podemos usar em conjunto.


1. operador de comparacao
2. operador logico
3. operador de range
4. operador de membros
5. operador de procura


### operadores

utilizados o operador de comparacao quando queremos comparar duas coisas

sintax de uma comparacao no sql: **expressao operador expressao**

tipos de condicoes:

1. coluna vs coluna: **nome = sobrenome**
2. condicao vs valor: **idade       >=     10** 
3. funcao vs valor: **UPPER(nome) = 'LUCAS'**
4. expressao vs valor : **preco * quantidade = 100**
5. subquery vs valor : **(select avg(sales) from vendas) = 1000**

#### operadores de comparacao

1. = : check se dos valores sao iguais
2. != : check se os valores nao sao iguais
3. > : check se um dos valores eh maior que o outro
4. >=: check se um dos valores eh maior ou igual ao outro
5. <: check se um dos valores eh menor que o outro
6. <=: check se um dos valores eh menor ou igual ao outro

#### operadores logicos

- And , Or e Not
Utilizados para criar duas ou mais condições

```sql 
select 
  category, products
from needful_things.orders
where products in ('pa','ra','dh') and values >= 1000 -- vai retornar dados apenas se todas as condições forem verdade

select 
  category, products
from needful_things.orders
where products  in ('pa','ra','dh') or cidade in ('sp','rj','ba') -- vai retornar dados apenas se uma das condições forem verdade

select 
*
from 
where products  not in ('pa','ra','dh')-- vai retornar dados invertendo a condicao,ou seja vai trazer tudo menos o que esta na lista (pa,ra,dh)
```

#### Range operador

utilizado para filtrar dados entre uma condicao e outra, seja um valor ou uma data (usado bastante com datas)

```sql: 
select 
  category, products
from needful_things.orders
where date between '01/01/2024' and '19/03/2024' 

**tudo que estiver abaixo da primeira condicao ou acima da segunda sera considerado falso e os dados nao serao retornados**
```

#### operador de 'listas'

- In e Not In
vai retornar de acordo com os valores passados

```sql 
select 
  category, products
from needful_things.orders
where products in ('pa','ra','dh') -- vai retornar somente dados que correspondem a essa lista

select 
  category, products
from needful_things.orders
where products not in ('pa','ra','dh') -- vai retornar tudo que não esteja aqui dentro
```

#### operador de 'pesquisa'

utilizamos o like para buscar um determinado padrao em um texto.

```sql 
select 
  category, products
from needful_things.orders
where products like '%uva%' -- pode ter "uva" tanto no começo quanto no fim

select 
  category, products
from needful_things.orders
where products like 'uva%' -- vai retornar algo caso tenha "uva" no começo

Select
  category, products
from needful_things.orders
where products like '%uva' -- vai retornar algo caso tenha "uva" no fim

Select
  category, products
from needful_things.orders
where products not like '%uva' -- vai retornar tudo que não tenha "uva" 
```

## Funções de agregações

Temos funções de agregações que realizam um determinado calculo no SQL.

- AVG(Média)

```sql 
select 
avg(salary) as média_salario
from needful_things.orders
where products in ('pa','ra','dh') and values >= 1000 -- vai retornar dados apenas se todas as condições forem verdade
```

- SUM(Soma)

```sql 
select 
sum(salary) as soma_salario
from needful_things.orders
where products in ('pa','ra','dh') and values >= 1000 -- vai retornar dados apenas se todas as condições forem verdade
```
- COUNT(Conta o conjunto)

```sql 
select 
count(funcionarios) as qtd_funcionarios
from needful_things.orders
where cidade in ('sp','bh','rj')  -- vai retornar dados apenas se todas as condições forem verdade
```
- MIN (Encontra o menor valor)

```sql 
select 
min(age) as menor_idade
from needful_things.orders
where products in ('pa','ra','dh') and values >= 1000 -- vai retornar dados apenas se todas as condições forem verdade
```

- MAX (Encontra o valor Máximo)

```sql 
select 
max(age) as maior_idade
from needful_things.orders
where products in ('pa','ra','dh') and values >= 1000 -- vai retornar dados apenas se todas as condições forem verdade
```

## Joins

Jois sao usados para combinar dados de uma ou mais tabelas atraves de campos em comum (como uma chave primaria ou estrangeira )

![joins](/dados/img/joins.png)


### Porque usar Joins?

1. combinar dados de tabelas diferentes em uma unica visao : inner - left
2. enriquecimento de dados 'buscar dados extras de outras tabelas' :  left
3. checkar a existencia 'filtrar' de um determinado dado em outra tabela : inner - left + where


#### Inner Join/Join

- é o join padrão do sql(podendo ser usado inner join ou somente join)
- Trazem os dados que correspodem as duas tabelas, tudo que as chaves não batam não vai trazer, tanto na tabela do from quanto da tabela do join.


#### Left Join

- mantem todos os dados da esquerda (tabela do from) e vamos tentar encontrar o que tem na direita (tabela do join)
- tudo que não tenha correspondencia vai trazer como Null(vazio)

#### Right Join

- mantem todos os dados da direta (tabela do join) e vamos tentar encontrar o que tem na direita(tabela do from)

- tudo que não tenha correspondencia vai trazer null

#### Full Join

- Tras todos dos dados de ambas as tabela
- o que não tem correspondencia vai trazer como Null(Vazio)

### Anti Joins

Anti Joins são usamos para nos ajudar a identificar/trazer os dados que não tem correspondencia(somente) entre as tabelas.

**Exemplo de uso: Você tem uma tabela de Clientes e uma tabela de Pedidos. Você quer encontrar todos os clientes que nunca fizeram nenhum pedido.**

### Left Anti Join
 
 semelhante ao Left Join, iremos usar a sintax com a diferença que pegamos os registros nulos da tabela de comparação (right)

```sql:

SELECT
    c.id_cliente,
    c.nome_cliente
FROM
    Clientes c
LEFT JOIN
    Pedidos p ON c.id_cliente = p.id_cliente
WHERE
    p.id_cliente IS NULL;

-- Essa consulta retornaria todos os clientes (com id_cliente e nome_cliente) que não possuem nenhum id_cliente correspondente na tabela Pedidos, ou seja, clientes que nunca fizeram pedidos.

```

### Right Anti Join

O Right Anti Join (também conhecido como RIGHT EXCLUDING JOIN) retorna todas as linhas da tabela da direita que não têm uma correspondência na tabela da esquerda, com base na condição de junção.

**Exemplo de uso:Imagine que você tem uma tabela Produtos e uma tabela Vendas. Você quer saber quais produtos não foram vendidos ainda.**

```SQL:

SELECT
    
FROM
    produtos
RIGHT JOIN
    vendas ON tabela_esquerda.coluna_comum = tabela_direita.coluna_comum
WHERE
    tabela_esquerda.coluna_comum IS NULL;;

-- Essa consulta retornaria todos oS pedidos (com id_cliente e nome_cliente) que não possuem nenhum id_cliente correspondente na tabela Pedclientes , ou seja, pedidos que não tem clientes atrelados.

```

### Full Anti Join

O Full Anti Join (também conhecido como FULL EXCLUDING JOIN ou SYMMETRIC DIFFERENCE) retorna todas as linhas de ambas as tabelas que não têm uma correspondência uma na outra, com base na condição de junção. É como dizer "me mostre o que é exclusivo de cada lado, mas não o que é comum

```SQL:

SELECT
    tabela_esquerda.*,
    tabela_direita.*
FROM
    tabela_esquerda
FULL OUTER JOIN
    tabela_direita ON tabela_esquerda.coluna_comum = tabela_direita.coluna_comum
WHERE
    tabela_esquerda.coluna_comum IS NULL OR tabela_direita.coluna_comum IS NULL

-- Essa consulta retornaria todos oS pedidos (com id_cliente e nome_cliente) que não possuem nenhum id_cliente correspondente na tabela Pedclientes , ou seja, pedidos que não tem clientes atrelados.

```

### Unions

No SQL temos os joins(junção de colunas) e os unions (junção de linhas), com algumas particularidades:

1 - Número de Colunas: Cada instrução SELECT dentro do UNION deve ter o mesmo número de colunas
2 - Ordem das Colunas: As colunas nas instruções SELECT devem estar na mesma ordem.
3 - Tipos de Dados Similares: As colunas correspondentes em cada instrução SELECT devem ter tipos de dados compatíveis (ou seja, você pode unir um VARCHAR com outro VARCHAR, ou um INT com um DECIMAL se a conversão for possível, mas não um VARCHAR com um INT diretamente sem um CAST).

**Exemplos de Uso:**

1 - Combinar Dados de Tabelas Semelhantes
2 - Consolidar Diferentes Tipos de Entidades em Uma Única Lista
3 - Criar Relatórios Unificados
4 - Análise de Dados de Log ou Eventos

#### Union

Com o union, podemos unificar uma ou mais tabelas em uma unica consulta

**Union quando aplicado retorna o dados sem duplicidade (aplica o distinct)**

```sql 

SELECT DISTINCT BAIRRO FROM TABELA_DE_CLIENTES
union
SELECT DISTINCT BAIRRO FROM TABELA_DE_VENDEDORES

```

**NO CASO ACIMA ESTAMOS UNINDO DUAS TABELAS ONDE TEM BAIRROS EM COMUM,TRAZENDO SOMENTE UM BAIRRO A + QUE NAO EXISTIA NA TABELA DE CLIENTES**

#### Union All

Podemos unir duas ou mais tabelas utilizando UNION ALL.

- Union NÃO aplica o distinct no retorno dos dados, ou seja vai trazer todos os dados correspondente nas tabelas

- temos que ter o mesmo numero de campos (e os tipos devem ser iguais) em ambas consultas

- os nomes das colunas são representados pela primeira consulta

## Funções

Dentro do sql temos funções built in, que nos ajuda em diversas tarefas, como converte textos, numeros e datas.

podemos dividir as funções em 2 grandes grupos:

1 - funções de linha unica: um unico valor entra -> um unico valor sai
2 - funçoes de multiplas linhas: varios valores entra -> sai um unico valor

**Podemos ter funções alinhadas: CAST(sum(valor) AS INT)**


### Funcoes de textos

Podemos dividir funcoes de textos em algumas subcategorias, como manpulacao, calculos e extracoes.

**1. Manipulacao:**

- Concat: combina varias srings em uma única

```SQL:


SELECT CONCAT ("Lucas",' ', 'Damasceno') -- LUCAS DAMASCENO


```

- Upper e Lower : transforma nossas strings em minúsculo ou minúsculo

SELECT LOWER(CONCAT ('LUCAS',' ' , 'DAMASCENO')) 


```SQL:


SELECT LOWER(CONCAT("LUCAS",' ', 'DAMASCENO')) -- lucas damasceno


```

- Trim: remove espaços em branco do inicio ou do fim de uma string

```SQL:


SELECT TRIM('    LUCAS DAMASCENO') -- LUCAS DAMASCENO  

```
**use o where first_name != trim(first_name) para identificar os casos que possuem espaço**

```SQL:

SELECT * FROM USUARIOS
where first_name != trim(first_name)

```

- replace: utilizado para substituir um determinado valor por outro

**A ORDEM é : string, valor antigo (-), novo valor (/)**

```SQL:

SELECT 

REPLACE('NOME','-',' ') AS NOME_CORRIGIDO,
CPF
 FROM USUARIOS


```

**2. Calculos:**

- Len: retorna a quantidade de caracteries tem uma determinada strings

```SQL:

SELECT LEN('LUCAS DAMASCENO DE OLIVEIRA') --27 --Espacos são considerados um caracter


```

**3. extracoes**


- Left and Right: Extrai(LEFT DO INICIO DA STRING, RIGHT PELO FIM DA STRING) caracteries de uma strings de acordo com o tamanho passado

```SQL:

SELECT LEFT('08229030000176',8) AS RAIZ_CNPJ -- 08229030

-- EXTRAIMOS APENAS OS 8 PRIMEIROS CARACTERIES DO CNPJ
```

 

- Substrings: extrai caracteries de acordo com a posição que foi indicada

**ORDEM : (valor/string , posicição inicial,tamanho(quantos carac)**

 ```SQL:

SELECT substring('42567209875',1,8) -- 42567209

-- passamos qual o inicio de que queremos extrair (1) e ate quantos caracteries (8)
```

### Funcoes de numeros

- Round: utilizado para arredondar valores para x casas decimais.

 ```SQL:

SELECT ROUND(VALOR_MENSALIDADE,2) --


```
 
- Abs: Transforma numeros negativos em positivos(atraves do numero absoluto)

 ```SQL:

SELECT ABS(-190.50) -- 190.50


```

### Funcoes de Data e Tempo

- Extracao em partes: Sao Funcoes Que Aajudam a Extrair Determinada Parte de uma data


 ```SQL:

SELECT YEAR('2025-07-07') -- 2025

SELECT MONTH('2025-07-07') -- 07

SELECT DAY('2025-07-07') -- 07

SELECT DATEPART(QUARTER,'2025-08-08') -- 3(TERCEIRO QUARTO)(RETORNA ESSAS INFOS EM INTEIROS)

SELECT DATENAME(MONTH,GETDATE())-- JULHO (RETORNA ESSAS INFOS EM TEXTOS, CORRESPONDENTE AO MES)

SELECT DATETRUNC(MINUTES, '2024-08-08 12:02:00') -- trunca a data , por exemplo, caso a data tenha minutos, usando o datetrunc, tudo que tem minutos eh 00

SELECT EOMONTH('2025-02-10')  -- 28 - RETORNA O ULTIMO DIA DO MES QUE FOI PASSADO

```

- Formatacao e Casting de datas

**1. Cast:**

**ORDEM: valor,tipo de dado**

Usamos o cast quando queremos mudar o tipo de dado para outros, exemplo: string para data, ou datetime para date

 ```SQL:

SELECT CAST(GETDATE() AS DATE) AS data_sem_horas -- 2025-07-10

-- o tipo de dados saiu de um datetime(data e hora) para date
```

**2. convert**

**ORDEM: tipo de dados,valor,estilo**

```SQL:

SELECT CAST(GETDATE() AS DATE) AS data_sem_horas -- 2025-07-10

-- o tipo de dados saiu de um datetime(data e hora) para date
```

Tambem permite conversoes de tipos de dados,mas permite aplicar um estilo (style) — um número que define o formato de exibição da data.


**3. format**

nos permite alterar tipos de dados 'localmente' como tipo de moeda, formato de datas.


```SQL:

SELECT FORMAT(GETDATE(), 'dd/MM/yyyy') AS Data_Formatada -- 10/07/2025;


```
**outro exemplo**
```SQL:

SELECT FORMAT(1234.5, 'C', 'pt-BR') -- R$ 1.234,50

```

**4. Calculos:**

-DateADD: Adiciona ou subtrai uma quantidade de tempo a uma data, como dias, meses ou anos.

**ORDEM: parte_data, quantidade, data_base**

```SQL:

SELECT DATEADD(DAY,30,GETDATE()) -- VAMOS ADICIONAR 30 DIAS COM BASE NA DATA ATUAL
SELECT
DATEADD(DAY,-180,GETDATE()) DATE_180, -- VAMOS DIMINUIR 180 DIAS COM BASE NA DATA ATUAL


```

- DateDIFF: Retorna a diferença entre duas datas em uma unidade de tempo especificada (ano, mês, dia, hora etc).


```SQL:


SELECT *,
DATEDIFF(YEAR,GETDATE(),BirthDate) as anos
 FROM [Sales].[Employees]

```


**5. validacao:**

- Isdate(): verificar se o dado passado eh uma data ou nao,

```SQL:

SELECT 
ISDATE('2025') checkName, -- 1 == true
ISDATE('123') checdate -- 0 == false

```


### Funcoes para tratar Nulos

**1. isNull:**

troca valores nulos por um valor especifico

**ORDEM: valor, valor_que_vamos_mudar**

```SQL:

SELECT ISNULL(NOME,'n/a') -- Aqui defininos um valor padrao
SELECT ISNULL(NOME,FULLNAME) -- aqui usamos outra coluna para ser o valor padrao

```

**Podemos usar o ISNULL para quando fazemos join com chaves que possuem valores nulos**

```SQL:
SELECT A.nome, B.cidade
FROM TabelaA A
LEFT JOIN TabelaB B
  ON ISNULL(A.id_cliente, -1) = ISNULL(B.id_cliente, -1)

```


**2. Coalese:**

 Transforma um valor nulo em valor padrão,forma mais elegante de trabalharmos com nulos

```sql 

SELECT * FROM STATION_DATA
WHERE coalesce(precipitation,0) =< 0.5; --usado no where

--caso a coluna precipitation tenha dados nulo, setamos o 0 para essas linhas
```

```sql 

SELECT report_code, coalesce(precipation,'n/a') FROM STATION_DATA

--caso o campo precipitation seja nulo, setamos o 'n/a' para essas linhas
```


**3. Is null e Is not null:**

- Is null é usado para verificar quando uma coluna tem valores nulos(vai retornar somente null)

```sql 
SELECT DISTINCT produtos FROM tb_products
where produtos is null;
```

- IS Not null é usado para quando não queremos trazer nulos

```sql 
SELECT DISTINCT produtos FROM tb_products
where produtos is not null;
```


## Case

Case é usado para criar uma estrutura lógico (como um if em outras linguagens), podemos utilizar essa logica para criar campos novos em nossas tabelas de acordo com certa regras.

```sql 

SELECT
PRODUTO,
PRECO,
CASE                                 
WHEN VALOR >50 AND VALOR <= 100 VALOR THEN 'BARATO'
WHEN VALOR > 100 THEN 'CARO'
ELSE VALOR END AS 'CATEGORIA_PRECO'
FROM VENDAS

```

**MODO ABREVIADO PARA EVITAR REPETICAO DA COLUNA(apenas para uma coluna)**                                                                                                        
```sql                                                                              
SELECT
PRODUTO,
PRECO,
CASE CIDADE
WHEN  'ALEMANHA' THEN 'DE' 
WHEN  'INDIA' THEN 'IN'  
WHEN  'BRASIL' THEN 'BR'  
WHEN  'ALEMANHA' THEN 'DE'  
ELSE 'N/A' END AS 'CIDADE'
FROM VENDAS

```



## Subqueries

O que são subqueries? 

- Subqueries(subconsultas) são queries dentro de outras, o entendimento é facil, o mais complicado é como aplicar isso:

- O resultado de uma subquerie é uma nova tabela

- É possivel usar subquery em um where(= / in), em um outro join

```sql 

SELECT * FROM MOVIMENTO
WHERE IN (
  SELECT CLIENTE * FROM CLIENTES WHERE NUM_FUNC = 10
)

```

**USANDO COMO OUTRA TABELA**

```sql 
select * from (
SELECT
CODIGO_DO_PRODUTO,
SUM(QUANTIDADE) AS RESUMO_QTD
FROM [dbo].[ITENS_NOTAS_FISCAIS]
GROUP BY CODIGO_DO_PRODUTO ) as teste
where teste.CODIGO_DO_PRODUTO = 394479

```

**USANDO DENTRO DO IN**
**SÓ PODEMOS USAR UMA SUBQUERY NO IN COM APENAS UM CAMPO**
```sql 
SELECT * FROM TABELA_DE_CLIENTES
WHERE BAIRRO IN (SELECT DISTINCT BAIRRO FROM TABELA_DE_VENDEDORES)

```

## Manipulações


### Format


### Convert

### Cast

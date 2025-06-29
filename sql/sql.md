# SQL - Sequel

Documentando meus estudos e projetos em SQL.

## Conceitos

### Normalização

Normalizamos tabela para que os dados sejam lidos e gravados de forma mais clara, ao invez de termos um unico tabelão de vendas, podemos dividir em diversas tabela, como produtos, vendedores, vendas, cliente.

### Chave Primaria e Chave Estrangeira

- Chave Primaria: Chave primaria identificar um registro unico em uma tabela (ID,CPF,NSU)
- Chave Estrangeira: Chave primaria de uma tabela que foi adicionado em outra tabela.

## Consultas (Querys)

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

```sql 
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

## Is Null e Is Not Null

- Is null é usado para verificar quando uma coluna tem valores nulos(vai retornar somente null)

```sql 
SELECT DISTINCT produtos FROM tb_products
where produtos is null;
```

- IS Not null é usadado para verificar quando não queremos trazer nulos
```sql 
SELECT DISTINCT produtos FROM tb_products
where produtos is not null;
```
## Case

Case é usado para criar uma estrutura lógico (como um if em outras linguagens)

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

## Coalese

- Transforma um valor nulo em valor padrão
- forma mais elegante de trabalharmos com nulos

```sql 

SELECT * FROM STATION_DATA
WHERE coalesce(precipitation,0) =< 0.5; --usado no where

```

**caso a coluna precipitation tenha dados nulo, setamos o 0 para essas linhas**

```sql 

SELECT report_code, coalesce(precipation,'n/a') FROM STATION_DATA

```
**caso o campo precipitation seja nulo, setamos o 'n/a' para essas linhas**

### Joins

Jois sao usados para combinar dados de uma ou mais tabelas atraves de campos em comum (como uma chave primaria ou estrangeira )

![joins](/dados/img/joins.png)


#### Porque usar Joins?

1. combinar dados de tabelas diferentes em uma unica visao : inner - left
2. enriquecimento de dados 'buscar dados extras de outras tabelas' :  left
3. checkar a existencia 'filtrar' de um determinado dado em outra tabela : inner - left + where


#### Inner Join/Join

- é o join padrão do sql(podendo ser usado inner join ou somente join)
- Trazem os dados que correspodem as duas tabelas, tudo que as chaves não batam não vai trazer, tanto na tabela do from quanto da tabela do join.


#### Left Join

- mantem todos os dados da esquerda (tabela do from) e vamos tentar encontrar o que tem na direita (tabela do join)
- tudo que não tenha correspondencia vai trazer como Null(vazio)


### Right Join

 - mantem todos os dados da direta (tabela do join) e vamos tentar encontrar o que tem na direita(tabela do from)
 - tudo que não tenha correspondencia vai trazer null


### Full Join

- Tras todos dos dados de ambas as tabela
- o que não tem correspondencia vai trazer como Null(Vazio)

### Union


Podemos unir duas ou mais tabelas utilizando UNION.
- Union aplica o distinct no retorno dos dados

- temos que ter o mesmo numero de campos (e os tipos devem ser iguais) em ambas consultas

- os nomes das colunas são representados pela primeira consulta

```sql 

SELECT DISTINCT BAIRRO FROM TABELA_DE_CLIENTES
union
SELECT DISTINCT BAIRRO FROM TABELA_DE_VENDEDORES

```
**NO CASO ACIMA ESTAMOS UNINDO DUAS TABELAS ONDE TEM BAIRROS EM COMUM,TRAZENDO SOMENTE UM BAIRRO A + QUE NAO EXISTIA NA TABELA DE CLIENTES**


### Union All

Podemos unir duas ou mais tabelas utilizando UNION ALL.
- Union NÃO aplica o distinct no retorno dos dados, ou seja vai trazer todos os dados correspondente nas tabelas

- temos que ter o mesmo numero de campos (e os tipos devem ser iguais) em ambas consultas

- os nomes das colunas são representados pela primeira consulta


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

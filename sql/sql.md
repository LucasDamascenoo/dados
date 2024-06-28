# SQL - Sequel

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

## Filtros

Quando trabalhamos com consultas, nem sempre vamos querer retornar tudo, as vezes queremos retornar dados atráves de uma determinada condição, para isso usamos o WHERE.

### Where
```sql 
select *
from needful_things.orders
WHERE SALES = 1000;

```
### Condições

Em conjunto com o where, temos condições adicionais que melhoram nossos filtros

- like e Not Like

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


- Between
Usado para retornar um intervalo (valores e datas)

```sql 
select 
  category, products
from needful_things.orders
where date between '01/01/2024' and '19/03/2024' 
```

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
```

## Aliases

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

### Limit

Limita a quantidade de registros em uma consulta SQL.

```sql 
select 
*
from needful_things.orders
LIMIT 5;
```

### Group By

Group by é responsavel por agrupar campos que possuam

## Manipulações


### Format


### Convert
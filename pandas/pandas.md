
# Pandas

Pandas é uma biblioteca do Python utilizado para analises e tratamento de dados.


# Series e Dataframes


: 


# Métodos de Dataframe

## head() - tail ()

- Com o df.head() somos capazes de ter um exemplo das 5 primeiras linhas do nosso dataframe, podemos comparar como o top ou limit do SQL.
- Já o df.tail() somos capazes de ter um exemplo das 5 ultimas linhas do nosso datagrame.

## info()

Com o df.info() conseguimos identifcar caracteriscas do nosso dataframe, como as colunas , seus tipos de dados, se os campos são nulos ou não.

## shape()

df.shape nos retorna a quantidade de colunas e linhas do nosso dataframe

## Value Counts()

 Value counts é responsavel por "contar" valores unicos em nosso dataframe:



## GroupBy()

- Permite agrupar uma determinada serie/coluna de um dataframe, assimo como no sql tambem precisamos de um função de agregação (sum,mean(média))

- Podemos agrupar informações e trazer valores de multiplas colunas ou apenas uma especifica ['Valor'],['Quantidade'] por exemplo

```{python}

groupby('Animal').sum(numeric_Only=True) #usamos esse parametro no sum caso não especificarmos uma coluna numerica

```


```{python}

groupby('Animal')[['Quantidade]].sum() ## incluindo [[]] criamos um DF

            Qtd
Animal      
A            30
B            40
C            10
```


## Query()

Com o query podemos selecionar dados em um dataframe atraves de uma condição, semelhante ao SQL.

**filtros sem query**

```{python}
df[df['nota']>= 6]
```

**Filtro por valor**
```{python}

df.query('NSU == 10101010')
```

**Filtro por valor + selecionando colunas especificas**

```{python}

df.query('rating > 100')[['name','rating']] 
```

**Filtro por uma determinada variavel**
```{python}

nsus = [101010,101020,1010130,50505050]
df.query['@nsus in NSU']  #USAMOS A VARIAVEL nsus(lista) para filtrar dados do campo Nsu
```

## Merge

No mundo dos dados nem sempre teremos as informações em um unico lugar e o pandas facilita a junção dessas informações de algumas maneiras:
Merge: é um metodo que une 2 ou mais dataframes de acordo com um campo em comum (chave) e o resultado disso são informações que os dataframes tenham em comum (como um join em sql)

### Tipos de junções

- Outer : O outer join retorna todas as linhas das duas tabelas, preenchendo com valores nulos onde não houver correspondência.

```{python}

df1 = pd.DataFrame({"key": ["A", "B", "C", "D"], "value1": [1, 2, 3, 4]})
df2 = pd.DataFrame({"key": ["B", "D", "E", "F"], "value2": [5, 6, 7, 8]})
unificado = pd.merge(df1,df2, on='key', how='outer')


# Retorno
key	value1	value2
0	A	1.0	NaN
1	B	2.0	5.0
2	C	3.0	NaN
3	D	4.0	6.0
4	E	NaN	7.0
5	F	NaN	8.0

```

- Left: retorna todas as linhas da esquerda(primeiro df no merge) e somente os valores correspondentes do segundo dataframe

```{python}
unificado = pd.merge(df1,df2, on='key', how='left')

# Retorno
key	value1	value2
0	A	1	NaN
1	B	2	5.0
2	C	3	NaN
3	D	4	6.0
```

- Right: O right join é o oposto do left join. Ele retorna todas as linhas da tabela da direita(segundo df) e as correspondentes da tabela da esquerda. Linhas da tabela da direita sem correspondência terão valores nulos.

### Chaves das junções

- On: usamos o On para especificar qual a coluna que queremos usar como chaves, **existe a possibilidade de termos chaves com nomes diferentes em cada df, ai usamos left e right**

```{python}
unificado = pd.merge(df1,df2, left_on='chave_df1', right_on='chave_df2', how='left')

```

**Mas e quando temos a chaves com o mesmo nome?**

Para esse "problema" temos um atributo suffixes usado para diferenciar qual coluna é de qual campo;

```{python}
unificado = pd.merge(df1, df2, on='chave', how='outer',
                     suffixes=('_esquerda', '_direita'))

# retorno 

chave	valor_esquerda	valor_direita
0	A	1.0	             4.0
1	B	2.0	             5.0
2	C	3.0	             NaN
3	D	NaN	             6.0

```


## Concat

Com o pd.Concat() podemos unir dois ou mais dataframes, esse método nos permite unidicar dfs sejam por linhas (um abaixo do outro) ou por colunas (um ao lado do outro)

- **Eixos:** Podemos concatenar nossos dataframes em dois eixos, horizontal axis=1 (colunas) e vertical axis=0 (linhas)


```{python}
df1 = pd.DataFrame({
    'chave': ['A', 'B', 'C'],
    'valor': [1, 2, 3],
    'data': ['01/01/2024','02/01/2024','03/01/2024']
})

df2 = pd.DataFrame({
    'chave': ['A', 'B', 'D'],
    'valor': [4, 5, 6]
})

unificado = pd.concat([df1,df2]).reset_index()

# retorno 

index	chave	valor	data
0	0	A	1	01/01/2024
1	1	B	2	02/01/2024
2	2	C	3	03/01/2024
3	0	A	4	NaN
4	1	B	5	NaN
5	2	D	6	NaN

```

- No processo acima unificamos dois dataframes que possuem a mesma estrutura de nomes, no caso um fico abaixo do outro, no df2 não tem informação de data e vem como NaN.

- Reset_index() foi usado para que os indexes sejam feito do "zero" pois sem isso, cada df terá seu index


**Exemplo onde as colunas não são a mesma**

```{python}
df1 = pd.DataFrame({
    'chave': ['A', 'B', 'C'],
    'valor': [1, 2, 3],
    'data': ['01/01/2024','02/01/2024','03/01/2024']
})

df2 = pd.DataFrame({
    'nsu': ['A', 'B', 'D'],
    'valor_nsu': [4, 5, 6]
})

unificado = pd.concat([df1,df2]).reset_index()

# retorno 

index	chave valor	data	nsu	valor_nsu
0	0	A	1.0	01/01/2024	NaN	NaN
1	1	B	2.0	02/01/2024	NaN	NaN
2	2	C	3.0	03/01/2024	NaN	NaN
3	0	NaN	NaN	NaN	A	4.0
4	1	NaN	NaN	NaN	B	5.0
5	2	NaN	NaN	NaN	D	6.0

```

- No Exemplo acima, como podemos notar os campos dos dfs não são o mesmo, então ele concatenou na forma de colunas (um ao lado do outro)



Quando concatenamos temos a possibilidade de 
## Rename(columns)


## Unique e Nunique()

- diferença entre ambos



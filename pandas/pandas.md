
# Pandas

Pandas é uma biblioteca do Python utilizado para analise e tratamento de dados.


# Series e Dataframes


: 


# Métodos de Dataframe

## info()
## shape()
## head()
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




## Value Counts()


## Rename(columns)


## Unique e Nunique()

- diferença entre ambos



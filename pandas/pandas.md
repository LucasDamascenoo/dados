
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

## Value Counts()


## Rename(columns)


## Unique e Nunique()

- diferença entre ambos




# Pandas

Pandas é uma biblioteca do Python utilizado para analises e tratamento de dados.

# Series e Dataframes

As principais estruturas de dados do Pandas são as Series e os Dataframes.

## Series

Uma Series é uma estrutura unidimensional que pode armazenar dados de qualquer tipo. Ela é semelhante a uma coluna em uma planilha ou a um vetor em programação. Cada elemento em uma Series é associado a um rótulo, chamado de índice.

Exemplo de criação de uma Series:

```python
import pandas as pd

s = pd.Series([1, 3, 5, np.nan, 6, 8])
```

## Dataframes

Um DataFrame é uma estrutura bidimensional que pode armazenar dados de diferentes tipos. Ele é semelhante a uma planilha ou a uma tabela de banco de dados, onde cada coluna representa uma variável e cada linha representa uma observação.

Exemplo de criação de um DataFrame:

```python
import pandas as pd

data = {'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
    'Idade': [25, 30, 35, 40],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília']}

df = pd.DataFrame(data)
```

Os Dataframes possuem várias funcionalidades, como a capacidade de filtrar, ordenar e agrupar os dados, além de realizar operações matemáticas e estatísticas.



# Métodos de Inspeção e Informações Básicas

## head() - tail ()

- Com o df.head() somos capazes de ter um exemplo das 5 primeiras linhas do nosso dataframe, podemos comparar como o top ou limit do SQL.
- Já o df.tail() somos capazes de ter um exemplo das 5 ultimas linhas do nosso datagrame.

## info()

Com o df.info() conseguimos identifcar caracteriscas do nosso dataframe, como as colunas , seus tipos de dados, se os campos são nulos ou não.

## shape

df.shape nos retorna a quantidade de colunas e linhas do nosso dataframe

# Manipulação de Dados

## GroupBy()

- Permite agrupar uma determinada serie/coluna de um dataframe, assimo como no sql tambem precisamos de um função de agregação (sum,mean(média))

- Podemos agrupar informações e trazer valores de multiplas colunas ou apenas uma especifica ['Valor'],['Quantidade'] por exemplo

```python

groupby('Animal').sum(numeric_Only=True) #usamos esse parametro no sum caso não especificarmos uma coluna numerica

```

```python

groupby('Animal')[['Quantidade]].sum() ## incluindo [[]] criamos um DF

            Qtd
Animal      
A            30
B            40
C            10
```

## Agregação(agg)

usamos agregações (agg) para aplicar uma ou mais função de agregação (sum,max,min)


```python:
df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

result = df.agg({
    'A': ['sum', 'mean'],
    'B': ['min', 'max']
})

#retorno
         A    B
sum   10.0  NaN
mean   2.5  NaN
min    NaN  5.0
max    NaN  8.

```

- Podemos tambem fazer agregações após um agrupamento de informações(groupby) retornando resultados agregados por cada grupo.

```python:
df = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B'],
    'Values': [1, 2, 3, 4]
})

result = df.groupby('Category').agg({
    'Values': ['sum', 'mean']
})

print(result)

#retorno
            sum mean
Category            
A             3  1.5
B             7  3.5

```

- Podemos tambem criar funções personalizadas:


```python:
def range_func(x):
    return x.max() - x.min()

df = pd.DataFrame({
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
})

result = df.agg({
    'A': ['sum', range_func],
    'B': ['min', 'max']
})

print(result)

#retorno
               A    B
sum         10.0  NaN
range_func   3.0  NaN # retorno da nossa função personalizada
min          NaN  5.0
max          NaN  8.0

```

## Query()

Com o query podemos selecionar dados em um dataframe atraves de uma condição, semelhante ao SQL.

**filtros sem query**

```python
df[df['nota']>= 6]
```

**Filtro por valor**
```python

df.query('NSU == 10101010')
```

**Filtro por valor + selecionando colunas especificas**

```python

df.query('rating > 100')[['name','rating']] 
```

**Filtro por uma determinada variavel**
```python

nsus = [101010,101020,1010130,50505050]
df.query['@nsus in NSU']  #USAMOS A VARIAVEL nsus(lista) para filtrar dados do campo Nsu
```


## Value Counts()

 Value counts é responsavel por "contar" a frequencia dos valores de um dataframe:

 ```python:
 
 s = pd.Series([1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

# Contando a frequência dos valores
contagem = s.value_counts()

print(contagem)

#retorno
4    4
3    3
2    2
1    1
 
 
 ```

- sort: tSe definido como False, não classifica os valores em ordem decrescente. Por padrão, o valor é True.

- dropna: Se definido como False, inclui contagens de valores NaN na saída. Por padrão, o valor é True, o que significa que NaN é excluído.




# Combinação de DataFrames


## Merge

No mundo dos dados nem sempre teremos as informações em um unico lugar e o pandas facilita a junção dessas informações de algumas maneiras:
Merge: é um metodo que une 2  dataframes de acordo com um campo em comum (chave) e o resultado disso são informações que os dataframes tenham em comum (como um join em sql)

### Tipos de junções

- Outer : O outer join retorna todas as linhas das duas tabelas, preenchendo com valores nulos onde não houver correspondência.

```python

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

```python
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

```python
unificado = pd.merge(df1,df2, left_on='chave_df1', right_on='chave_df2', how='left')

```

**Mas e quando temos a chaves com o mesmo nome?**

Para esse "problema" temos um atributo suffixes usado para diferenciar qual coluna é de qual campo;

```python
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


```python
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

```python
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

## Join

# Limpeza e Transformação de Dados

## Criando Colunas novas

- Quando trabalhamos com dataframe temos a capacidade de adicionar novas colunas em nosso df.


```python
df1 = pd.DataFrame({
    'chave': ['A', 'B', 'C'],
    'valor': [1, 2, 3],
    'data': ['01/01/2024','02/01/2024','03/01/2024']
})


df1['Produto'] = ['porta','massa corrida'] # criamos uma coluna nova com a lista de produtos

```

## Rename(columns)

Com o rename podemos renomar colunas/series dos nossos dataframes.

```python
df.rename(columns={'old_name': 'new_name'}, inplace=True)

```

## drop_duplicates()

Quando trabalhamos com dados as vezes nos deparamos com dados duplicados e para isso temos métodos que nos ajudam com isso:

subset : utilizado para especificar quais (uma ou mais) colunas nas quais vamos procurar duplicatas.


## Conversão de tipos

Existem vários métodos de conversão de tipos no pandas. Alguns dos principais são:

- `astype()`: Este método é usado para converter o tipo de dados de uma coluna em um tipo de dados específico. Por exemplo, `df['coluna'].astype(int)` converte a coluna em um tipo inteiro.

- `to_numeric()`: Este método é usado para converter uma coluna em um tipo numérico. Ele lida com valores não numéricos, como strings, e os converte em NaN (Not a Number) ou em um valor numérico, se possível.

- `to_datetime()`: Este método é usado para converter uma coluna em um tipo de data e hora. Ele pode lidar com diferentes formatos de data e hora e converter a coluna em um objeto de data e hora do pandas.

- `to_timedelta()`: Este método é usado para converter uma coluna em um tipo de duração de tempo. Ele pode lidar com diferentes formatos de duração de tempo e converter a coluna em um objeto de duração de tempo do pandas.

- `to_string()`: Este método é usado para converter uma coluna em uma representação de string. Ele converte os valores da coluna em strings.

Esses são apenas alguns dos principais métodos de conversão de tipos no pandas. Existem outros métodos disponíveis, dependendo das necessidades específicas de conversão de tipos. 

## fillna()

- Tambem podemos "filtrar" valores NaN e modificar por valores "padrão" utilizando o fillna()

```python:
df.fillna({
    'idade':0,
    'renda': "N informado"
})

# transformando o que está NaN em idade para 0 e renda como não informado

```
## dropna()

- Dropaaa remove valores que estão como na em um dataframe

```python:
df2 = df.dropna(subset=["nome", "renda"], how="any")
df2

```
- subset: defini as colunas que vamos fazer o "check" de na e dropar os valores
- how: defini como vai ser a regra de exclusão: any ( vai dropar qualquer valor Nan caso exista em uma das colunas ), all (vai dropar se as ambas as colunas tenham valores nan)

## isna() e notna()

 - Podemos verificar se existem valores NaN em nossos dataframes utilizando o isna()

```python:

df['idade'].isna().value_counts()
df['idade'].isna().sum()
df.isna().sum()

```
## duplicated()


# Outras Funcionalidades

## Unique e Nunique()

 - Usamos o nunique() para saber quantos valores unicos tem em uma determinada coluna(serie)

 - Já o unique vai retornar uma lista com os valores unicos

## Sort_Values()

## pivot() e pivot_table()

## melt()
## apply()

com o método apply podemos aplicar uma função(até mesmo uma lambda) no nosso dataframe:



## map()
## applymap()
## crosstab()





# Porque Python?

- Python é uma linguagem de programaçao open source, de sintax facil "proxima" a humana
- usada em diversos campos (dados, web, ML, web scrapring)
- possui diversas bibliotecas como (pandas, numpy, spark, openxlx)


# Tipos de dados

Toda linguagem de programaçao possui tipos de dados e as do python sao as seguintes:

**Single Value**

- **str**: cadeia e caracteriries:  'uma string' "outra string"
- **int**: numeros inteiros(positivos ou negativos): 10, -10, 1000
- **floats**: numeros decimais (positivos ou negativos): 10,5 , 10.0, -100.2
- **bool**: sao valores boleanos(True ou False)

**Multiple Values**
- **list**: um conjunto de dados agrupados em uma unica variavel: [1,2,3,4]
- **dict**: sao nosso dicionarios, onde guardamos dados atraves de chaves e valores
- **tuple**:
- **range**: 
- **set**: 


## Type

Podemos verificar qual o tipo de dados estamos trabalhando atraves da funçao(built-in) type:

```python:

type(1) #int
type('hello') #str

```

## Type Casting

Podemos modificar os tipos de dados efetuando o type casting:

```{python}

entrada = input("digite o valor") #aqui sempre vai retornar uma string

#type casting

entrada = float(input("digite o valor")) #convertemos string para float

```

# Variaveis

Variáveis são espaços na memória onde guardamos dados. Essas variáveis podem ser acessadas posteriormente, permitindo a criação de lógica com elas.

Em python criamos vartiaveis da seguinte forma:


```{python}

age = 29
nome_completo  = 'Lucas Damasceno'

```
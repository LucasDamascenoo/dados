
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

# Strings

Vamos aprender a trabalhar/usar metodos de strings.

## Slicing

O slicing em Python é uma técnica para acessar partes de sequências, como strings, listas e tuplas. Ele permite extrair subpartes dessas sequências de maneira eficiente e legível.

**Sintaxe Básica**

A sintaxe básica para slicing é:
```python
sequencia[inicio:fim:passo]


nome_completo  = 'Lucas Damasceno'

print(nome_completo[0:5]) #Lucas

# reventendo uma string
print(uma_string_muito_grande[::-1])

```

## Outros Métodos

- **upper()**:converte a string para maisculo
- **lower()**:converte a string para minusculo
- **len()**: monstra a quantidade de caracteries tem uma string
- **strip()**: remove espaços em branco de uma string
- **replace()**: altera o valor passado para outro
- **find()**: procura um valor passado na string e retorna seu indice, caso nao tenha retorna -1
- **split**: Divide a string em uma lista de substrings com base em um delimitador.
**Nenhum desses metodos mudam o valor original da variavel que foi aplicada, pois strings sao imutaveis**


# Condicionais

Estruturas condicionais nos permite tomar caminhos diferentes em nossas aplicaçoes, se isso for aquilo, faça isso, senao faça aquilo outro;

```python

if condiçao:
    codigo que vai executar se a condiçao for verdadeira
elif:
    cria um novo bloco de código que vai executar caso for verdade
else:
    o codigo que estiver aqui executa caso o codigo do if/elif for falso

```

**ternarios**

com o ternario podemos simplificar o codigo quando precisamos criar uma condicional simples (if/else)

```python

idade = 29

'adulto' if idade >= 18 else 'criança'

```

**short circuit**

O "short circuit" (ou "avaliação de curto-circuito") em Python refere-se ao comportamento dos operadores lógicos `and` e `or` ao avaliar expressões booleanas. Em uma expressão de curto-circuito, a avaliação para assim que o resultado é conhecido, sem avaliar o restante da expressão.

**Exemplos**

**Operador** `and`
```python
a = False
b = True

resultado = a and b
print(resultado)  # Saída: False (a avaliação para após a primeira expressão)

```


# Funçoes

Funçoes sao blocos de códigos que executam um programa, essas funçoes podem ser chamadas em qualquer parte do nosso código, dentro de outra funçao, nos ajuda a criar blocos de codigo logicos, diminuindo repetiçoes e deixando nosso código mais organizado:



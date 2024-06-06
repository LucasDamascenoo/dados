# Day02

O que aprendemos hoje?

## Tipos de dados

Conhecemos os tipos de dados básicos de python:

- Str : São cadeias de carecteries ("Texto")
- Int : Números inteiros (10, 200)
- Floats: Números decimais (10.5)
- Bool : São os valores booleanos (True e false)

## Operador Type()

Operador type verificar o tipo de dado que foi passado pra expressão type("Strings") = str

## Type Casting

Podemos modificar os tipos de dados efetuando o type casting:

```{python}

entrada = input("digite o valor") #aqui vai retornar uma string

#type casting

entrada = float(input("digite o valor")) #convertemos string para float

```

## Operadores Matematicos

- - adição
- - subtração
- / divisão
- - multiplicação
- \*\* exponenciação
- % resto da divisão

## F'strings

Com f'strings podemos vacilitar a concatenação de variaveis e arredendodamento de casas decimais

```{python}

entrada = input("digite o valor") #aqui vai retornar uma string

print(f" sua entrada foi {entrada:2.f}")

```

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

Com f'strings podemos facilitar a concatenação de variaveis e arredendodamento de casas decimais

```{python}

entrada = input("digite o valor") #aqui vai retornar uma string

print(f" sua entrada foi {entrada:2.f}")

```

# Day03

O que aprendemos hoje?

## Estrutura condicional

Estrutura condicional nos permite criar blocos de códigos atráves de certas condições, se for verdadeiro faça isso, se for falso faça aquilo.

```{python}

idade = input("qual sua idade? ") #aqui vai retornar uma string


if idade >= 18:
  print("você pode entrar na balada")
else:
  print("você não pode entrar na balada")

```

- if : se condição for true faça isso
- elif: se nao se (cria outra condição)
- else : se a condição for false faça aquilo

### Estrutura condicional alinhada

Podemos ter mais de uma condição atrelada a um if:

altura = int(input("Digite sua altura "))

```{python}
if altura >=170:
  print("Pode entrar")
  age = int(input("Qual a sua idade? "))
  if age <= 18:
    print("valor do ticket é $15")
  else:
    print("valor do ticket é $20")
else:
  print(" Não pode entrar")

```

No exemplo acima primeiro ele da check na altura, caso passe ele faz outra validação de idade para ver a idade e passar o preço de acordo com a determinada idade,
caso nem passe na primeira validação, cai direto no else da altura e define que o cliente não pode entrar

## Operadores condicionais

Os operadores condições nos ajuda na criação de condições (preposições).

- AND : todas as condições passadas precisam ser verdadeira para retornar True
- OR : apenas umas das condições passadas precisam ser verdadeira pra retornar True
- NOT: inverte a operação se for True > False e se for False > True
- IN: Verifica um determinado valor, caso exista True, caso não False
# Day04

## Random

Podemos gerar números de forma "aleatoria" que por trás dos pano usa o algoritmo Mersenne Twister.

```{python}

import random #primeiro precisamos importar o módulo random

aleatorio = random.randint(1,10) # gere um numerod entre 1 e 10


```

## Listas

Lista é uma estrutura de dados capaz de armazenar uma lista de dados organizada.

```{python}
frutas = ['Maça','Banana','Uva'] #lista de frutas
```

### Indices

Quando criamos uma lista, os valores guardados dentro dela, pode ser acessada por seus indices (em linguagem de programação começa com 0)

```{python}


frutas = ['Maça','Banana','Uva'] #lista de frutas

frutas[0] Maça
frutas[1] Banana
frutas[3] Uva
frutas[10] IndentationError: unexpected indent

```

### Metodos de listas

- len() : Ve a qtd de elementos em uma lista
- append(): add um valor no fim da lista
- extend() - add varios elementos no fim da lista


## Dicionarios

São um conjunto de dados que contem chaves e valores:


```{python}
aluno = {"matricula": 101010101,
         "dia_cadastro": 25,
         "mes": 10,
         "turma": "2e"}
```

**acessando o valor de uma determinada chave**
```{python}
print(aluno["matricula"])
```

**alterando o valor de uma determinada chave**
```{python}

aluno["turma"] = "3f"
```

**adicionando uma nova chave valor**

```{python}

aluno["modalidade"] = "Presencial"

```

### Listas em dicionarios

```{python}

loja = {'nomes': ['televisão', 'celular', 'notebook', 'geladeira', 'fogão'],
        'precos': [2000, 1500, 3500, 4000, 1500]}

```

### Metodos de dicionarios

- pop(): remove a chave/valor de um dicionario
- items(): retorna uma lista dos pares(chave e valor)
- keys(): retorna todas as chaves do dicionario
- values(): retorna todos os valores de um dicionario


# Day05

## Loops

Podemos rodar um determinado bloco de códigos "inumeras" vezes de acordo com seu tamanho por exemplo, e para isso usamos loops

### For

For é bastante utilizado principalmente para trabalhar com listas, vamos a alguns exemplos:

- Utilizado para iterar um conjunto de dados

**Sintax**
```{python}
for elemento in conjunto: 

  #elemento sera repetido(individualmente) até o fim do conjunto
```
**Exemplo**
```{python}
animals = ['cat', 'window', 'defenestrate']

for animal in animals:
  print(animal)
```

1 - primeiro criamos uma variavel que vai receber o valor cada vez que o loop rodar (animal)

2 - declaramos o que vamos iterar : lista animals

3 - printamos a variavel que criamos no primeiro passo

#cat
#window
#defenestrate


### For + Range

- podemos utilizar o for em conjunto com o range(cria valores) de acordo com um limite(range) passado

```{python}
for e in range(1, 11):
    print(e)
```

### While

- While é utilizado para repetir um determinado código enquanto uma certa condição for verdadeira

**Sintax**
```{python}
while condição:
  #faça isso
```

**Exemplo**

```{python}
contador =  1
while contador <=10:
  print(contador)
  contador+=1
```
**Exemplo pratico**

```{python}
contador = 1

while contador <= 3:
    n1 = float(input("Digite sua primeira nota: "))
    n2 = float(input("Digite sua segunda nota: "))
    print(f'Média: {(n1+n2)/2}')
    contador += 1
```


# Day06

## Funções

Funções é um bloco de código que executa um subprograma que pode ser reutilizavel em diversas partes dos nossos códigos.



### Elemento essenciais de uma função

1. "def": define a função
2. "soma": toda função precisa de um nome
3. "argumentos": são as variaveis internas da nossa função(opcional)
4. "processamento" : é o que incluimos dentro da função, sera o executavel da nossa função
5. "return": 

### Divisão de uma função

uma função basicamente é divida em duas partes, cabeçalho e corpo da função, onde o cabeçalho é o que chamamos e o corpo é o executavel

- Cabeçalho 

```Python:

def extract_audio (video_file:str, output_file: str, eq:bool = True) 
=> Path | tuple[Path...]:

```

1. **Nomes**: como nomeamos nossas funções
- Não podem iniciar com numeros e caracteries especieis(exeto o _)
- letras minusculas
- devemos usar snake_case

2. **Parametros**: Parametros são "variaveis" internas de uma função
- Temos diversos tipos de parametros, como o posicial (de acordo com a ordem definida) e chaves chave-valor (x=1,y=2)

3. **Anotação de parametros**: a partir do py 3.5 podemos definir tipos pros nossos parametros (valor:float,taxa:float)





## List Comprehesion

- Podemos gerar listas de forma "automatica" atraves do list comprehension


```Python:

list1 = [1,2,3,4,5]

listComp = [x**2 for x in list1] ## aqui vamos gerar uma lista do dobro de uma lista dado anteriormente.


```
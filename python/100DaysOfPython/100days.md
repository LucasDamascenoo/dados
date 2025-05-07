

# Dia 04

## Random

Random eh um metodo do Python que nos permite criar numeros de forma 'aleatorio' (python usam o Metodo Mersene Twister) para criar essa aleatoridade.

1 - precisamos importar o metodo random

```{python}:

import random


aleatorio = random.randint(1,10)

aleatorio2 = random.random()
```

aleatorio  : aceita 2 parametros, 1 numero inicial e 1 final (incluso) no qual o programa vai gerar um aleatorio dentro desse range escolhido.
aleatorio2: gera um numero aleatorio (float) entre 0.0 e 1.0

***crie um programa que determina aleatoriamente cara ou coroa**

```{python}:

cara_coroa = random.randint(0, 1)

if cara_coroa == 0:
    print('cara')
else:
    print('coroa')

```


## List

List is a python data structure, que nos permite guardar diversos dados em uma lista unica variavel.

Anteriormente aprendermos que para guardar valores usavamos variavel (como o exemplo acima), mas note que quando queremos criar um grupo de dados, repetimos multiplas variavel, como isso tem as listas.


```{python}:


nome = 'lucas'
nome_esposa = 'Tatiane'

nome_familia = ['Lucas','Tatiane','Bruce']

```

***adicionando um elemento no final da lista**

1. Adiciona um elemento no final
numeros.append('Mary')

*** escolha aleatoriamente um nome na lista de amigos para pagar a conta**

```{python}:

import random 
lista_amigos = ['Brandao','Prandi','Kayk','Felipe NaRIZ','Mumu']

roleta_russa = random.choice(lista_amigos)

print(f' o escolhido para pagar a conta foi {roleta_russa}')


```


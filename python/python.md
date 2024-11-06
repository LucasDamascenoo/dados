
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

# Loops

Loops são estruturas de controle em Python que permitem a execução repetida de um bloco de código enquanto uma condição é verdadeira ou para cada item em uma sequência.

## For Loop

O `for` loop é usado para iterar sobre uma sequência (como uma lista, tupla, string, ou range). É útil quando sabemos o número de iterações ou queremos iterar sobre cada item de uma sequência.

```python
# Exemplo de for loop iterando sobre uma lista
frutas = ['maçã', 'banana', 'cereja']
for fruta in frutas:
    print(fruta) # Saída:# maçã # banana # cereja


# Exemplo de for loop usando range
for i in range(5):
    print(i) # Saída:# 0 # 1 # 2 # 3 # 4

```

## While Loops

O `While loop` é usado para repetir um bloco de código enquanto ele for verdadeiro, podemos usar o while em condiçoes que nao sabemos o numero exatos de iterações:

```python

contador = 0
while contador < 5:
    print(contador)
    contador += 1

```

## Break e Continue

**Break**: A instrução break é utilizada para interromper a execução de um loop, saindo imediatamente dele.

```python

while True:
    user_input = input("Digete uma frase (q para sair) ")
    if user_input == 'q'
        break
    print(f'Seu texto foi {user_input}')    

```

**Continue**: A instrução continue é utilizada para pular a iteração atual do loop e passar para a próxima iteração. Ao encontrar um continue, o código restante dentro do loop para aquela iteração é ignorado.

```python

numeros = range(10)

for numero in numeros:
    if numero % 2 != 0:
        continue  # Ignora números ímpares
    print(f"Número par: {numero}")  

```


# Listas

Em python tem um conceito em listas chamados List Comprehensions, que é uma maneira de criar listas de forma "facil"

```python

list_comp = [x for x in range(1, 11)]

print(list_comp)  # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

```
- No exemplo acima, criamos a expressão `x`, que representa cada item na sequência que estamos iterando. Passamos `x` para iterar sobre a sequência fornecida (como uma lista, tupla ou range). A expressão `x` é avaliada para cada item na sequência, e o resultado é adicionado à nova lista.

# Tuplas

Tuplas tbm é uma estrutura de dados, semelhante as listas (arrays) tuplas tbm guarda valores de qualquer tipo, mas vamos as diferenças:


**Imutavel**: Depois que você cria uma tupla, não é possível modificar seus elementos.

**Definida com Parênteses**: A sintaxe de uma tupla utiliza parênteses () para criar uma sequência de elementos.

**Leve e Rápida**: Por ser imutável, uma tupla pode ser processada mais rapidamente que uma lista, e também consome menos memória.

**Permite Qualquer Tipo de Dado**: Assim como listas, tuplas podem conter qualquer tipo de dado — inteiros, strings, outras tuplas, etc.

```python

minha_tupla = (1, 2, 3, 'a', 'b')

print(minha_tupla)  # Saída: (1, 2, 3, 'a', 'b')

```

## Pora que usar tuplas?

1. Dados que não devem ser alterados: Se você quer garantir que certos dados permaneçam constantes, use tuplas. Como elas são imutáveis, seu conteúdo não será modificado acidentalmente.

2 . Melhor desempenho: Tuplas são mais eficientes que listas em termos de velocidade e uso de memória. Em situações de alto desempenho, onde você só precisa armazenar e ler dados, elas podem ser mais rápidas.

3 . Chaves em dicionários: As tuplas podem ser usadas como chaves em dicionários, pois são imutáveis, ao contrário das listas (que não podem ser usadas como chaves).

**Dados Imutaveis**:
```python

# DADOS IMUTAVEIS
coordenadas = (40.7128, -74.0060)

```
**Funções com Retornos Múltiplos**:Quando uma função retorna vários valores, é comum usar uma tupla:

```python

def calcular_area_perimetro(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro  # Retornando como tupla

resultado = calcular_area_perimetro(5)
print(resultado)  # Saída: (25, 20)

```

**Usando tuplas como chaves de dicionário**:

```python

pessoas = {
    ('João', 'Silva'): 28,
    ('Maria', 'Oliveira'): 34
}
print(pessoas[('João', 'Silva')])  # Saída: 28

```



# Funçoes

Funçoes sao blocos de códigos que executam um programa, essas funçoes podem ser chamadas em qualquer parte do nosso código, dentro de outra funçao, nos ajuda a criar blocos de codigo logicos, diminuindo repetiçoes e deixando nosso código mais organizado:



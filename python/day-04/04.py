
import random

## NUMERO ALEATORIO INTEIRO
aleatorio = random.randint(1,10) #vai gerar um numero aleatorio entre 1 a 10


print(aleatorio)

float_aleatorio = random.random()* 5 + 1

print(float_aleatorio)


## DESAFIO 01

coin = random.randint(0,1)

if coin == 1 :
  print("Heads")
else:
  print("Tails")
  
  # Listas
  
  estados_brazil = ['sao paulo', 'rio de janeiro','minas gerais','coritiba','amazonas','bahia']
  estados = ['rio grande do sul','brasilia','ceara']
  
  print(estados_brazil + estados)
  
  print(estados_brazil[-1])
  print(estados_brazil[10])
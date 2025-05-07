
import random


# aleatorio = random.randint(1, 10)
# aleatorio_float = random.random() * 10


# print(aleatorio_float)

# print(aleatorio)

# frutas = ["maçã", "banana", "laranja"]
# print(random.choice(frutas))


cara_coroa = random.randint(0, 1)

if cara_coroa == 0:
    print('cara')
else:
    print('coroa')


lista_amigos = ['Brandao', 'Prandi', 'Kayk', 'Felipe NaRIZ', 'Mumu']

roleta_russa = random.choice(lista_amigos)

print(f' o escolhido para pagar a conta foi {roleta_russa}')

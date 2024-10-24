# Exercícios sobre Loops

# 1 - Contagem Regressiva
# Escreva um programa que utiliza um loop while para fazer uma contagem regressiva de 10 a 1. No final, imprima "Feliz Ano Novo!".

contator = 10

while contator >= 1:
    print(contator)
    contator -= 1
print("Feliz Ano nuevo")

# 2 - Soma de Números
# Crie um programa que solicita ao usuário que insira números (utilizando um loop while). O loop deve parar quando o usuário digitar 0 e, em seguida, imprimir a soma de todos os números inseridos.

soma = 0

while True:
    num_usuario = int(input("Insira um numero "))
    if num_usuario == 0:
        break
    soma += num_usuario
print("A soma dos números é:", soma)

# usamos o while true, para que o bloco de código seja "infinito" até que a condiçao  do break seja atendida e  só ai o loop é encerrado:

# 3 - Fatorial de um Número
# Escreva uma função que calcule o fatorial de um número inteiro positivo utilizando um loop for. O usuário deve inserir o número.

# 4 - Imprimir Números Pares
# Utilize um loop for para imprimir todos os números pares de 1 a 50.

# 5 - Tabuada
# Crie um programa que pede ao usuário um número inteiro e utiliza um loop for para imprimir a tabuada desse número (de 1 a 10).

# 6 - Contar Dígitos
# Escreva um programa que utiliza um loop while para contar quantos dígitos um número inteiro possui. O número deve ser inserido pelo usuário.

# 7 - Média de Números
# Crie um programa que solicita ao usuário que insira números (utilizando um loop while). O loop deve parar quando o usuário digitar 0 e, em seguida, imprimir a média de todos os números inseridos.

# 8 - Números Primos
# Escreva um programa que utiliza um loop for para encontrar todos os números primos entre 1 e 100.

# 9 - Fibonacci
# Crie um programa que utiliza um loop for para gerar os primeiros 20 números da sequência de Fibonacci.

# 10 - Inverter String
# Escreva um programa que utiliza um loop for para inverter uma string fornecida pelo usuário.



# # for item in iteravel:
# #     bloco de código que será executado:


# for number in range(10):
#     print(number)


# for char in "Lucas Damasceno de Oliveira":
#     print(char)


# # while loops

# count = 1


# while count <= 10:
#     print(count)
#     count += 1

# while True:
#     user_input = input("Escreva algo (q para sair): ")
#     if user_input == 'q':
#         break
#     print(f'voce digitou:{user_input} ')


# for n in range(1, 10):
#     if n == 2:
#         print("o 2 foi skipada")
#         continue
#     print(n)


numeros = range(10)

for numero in numeros:
    if numero % 2 != 0:
        continue  # Ignora números ímpares
    print(f"Número par: {numero}")

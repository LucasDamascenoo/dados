import math

# Definindo os valores
z = 1.96
sigma = 4
n = 100

# Calculando a margem de erro
margem_erro = z * sigma / math.sqrt(n)

# Exibindo o resultado
print(f"A margem de erro é: {margem_erro}")

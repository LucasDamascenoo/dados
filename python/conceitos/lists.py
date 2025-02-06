

list_comp = [x for x in range(1, 11)]

print(list_comp)


lista_produtos = ['televisão', 'som portatil', 'dvd']

lista_produtos.append('video game')


for produto in lista_produtos:
    print(produto)


def calcular_area_perimetro(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro  # Retornando como tupla


resultado = calcular_area_perimetro(5)
print(resultado)  # Saída: (25, 20)
print(type(resultado))

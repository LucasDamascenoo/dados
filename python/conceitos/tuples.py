
# como remover item de uma tupla

minha_tupla = (1, 2, 3)


def remove_item(minha_tupla, value):
    # transformando tupla em lista
    minha_listsa = list(minha_tupla)
    minha_listsa.remove(value)
    # transformando lista em tupla
    return tuple(minha_listsa)


print(minha_tupla)
print(remove_item(minha_tupla, value=2))


def calcular_area_perimetro(lado):
    area = lado ** 2
    perimetro = 4 * lado
    return area, perimetro  # Retornando como tupla


resultado = calcular_area_perimetro(5)
print(resultado)  # Saída: (25, 20)

print(type(resultado))



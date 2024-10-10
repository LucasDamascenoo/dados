
uma_string_muito_grande = 'aqui tem uma string muito grande, vamos aprender indixes e slicing'
string_teste = 'abcdef'


# estamos "fatiando " a string a partir do indice 2 até o final (pois nao passamos o fim :)
print('tinker'[1:4])

# pegando os ultimos indices

numeros = '123456789'
print(numeros[-4])

# pulando caracteries
# comecei no indice 1(b) fui até o 4(d) e pulei 2 indices (2-3) parando no ultimo
print(string_teste[1:4:2])


string_teste = "ghtj"


# sprit

poema = 'o-rato-roeu-a-roupa-do-rei-de-roma'

print(poema.split(' '))


def somaSalario(salario):
    return (salario * 0.2) + salario


print(somaSalario(4300))

# reventendo uma string
print(uma_string_muito_grande[::-1])

print('Lucas Damasceno'[0:5])
print('Lucas Damasceno'.find('s'))
print('Lucas Damasceno'.replace('Damasceno', 'Oliveira'))


texto = "Olá, mundo! Bem-vindo ao Python."

print(texto.split())

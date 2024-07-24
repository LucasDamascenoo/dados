# %%
import pandas as pd
import numpy as np
# %%
df = pd.read_csv('../data/customers.csv', delimiter=';')

# %%
df['Double Points'] = df['Points'] * 2
df
# %%
df['Constante'] = 1
df


# %%
# como transforma a coluna nome em maisculo
df['Name'].str.upper()
# %%
# pegar todos os elementos e pegar o primeiro nome antes de _


def get_first(nome):
    return nome.split("_")[0]


# apply aplica uma função nos nossos elementos(cada elemento)
# df['Name'].apply(get_first)
df['Name'].apply(lambda nome: nome.upper().split("_")[0])
# explicando a função: vamos criar nossos nomes em caixa alta(upper)
# e em sequencia dividir o nome em uma lista[0] onde pegamos somente o primeiro


# %%
# criando uma coluna de acordo com a faixa pontos

def intervalo_pontos(pontos):
    if pontos < 2500:
        return 'baixo'
    elif pontos < 3500:
        return 'medio'
    else:
        return 'alto'


df['Faixa de POntos'] = df['Points'].apply(intervalo_pontos)
df

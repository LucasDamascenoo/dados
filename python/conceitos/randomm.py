
import random
import pandas as pd
import os

# # aleatorio = random.randint(1, 10)
# # aleatorio_float = random.random() * 10


# # print(aleatorio_float)

# # print(aleatorio)

# # frutas = ["maçã", "banana", "laranja"]
# # print(random.choice(frutas))


# cara_coroa = random.randint(0, 1)

# if cara_coroa == 0:
#     print('cara')
# else:
#     print('coroa')


lista_amigos = ['Brandao', 'Prandi', 'Kayk', 'Felipe NaRIZ', 'Mumu']

roleta_russa = random.choice(lista_amigos)


dados = pd.DataFrame(lista_amigos)

pasta_downloads = os.path.join(os.path.expanduser('~'), 'Riot Games')

# Monta o caminho completo do arquivo
caminho_arquivo = os.path.join(pasta_downloads, 'dados.xlsx')

# Salva o Excel lá
dados.to_excel(caminho_arquivo, index=False)

# %%
import pandas as pd
import os
# %%

df1 = pd.DataFrame({
    'chave': ['A', 'B', 'C'],
    'valor': [1, 2, 3],
    'data': ['01/01/2024','02/01/2024','03/01/2024']
})

df2 = pd.DataFrame({
    'nsu': ['A', 'B', 'D'],
    'valor_nsu': [4, 5, 6]
})
# %%
unificado = pd.merge(df1, df2, on='chave', how='outer',
                     suffixes=('_esquerda', '_direita'))
# %%
unificado = pd.concat([df1,df2]).reset_index()
unificado
# %%
dados = []

for arquivos in os.listdir(r'C:\Users\fb.11129\OneDrive - Elo Participações LTDA\Área de Trabalho\dsfs'):
    df = pd.read_excel(arquivos)
    dados.append(df)

concatenado = pd.concat(dados,ignore_index=True)

# %%

# %%

# %%

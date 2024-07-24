# %%
import pandas as pd
import os
# %%

df1 = pd.DataFrame({
    'chave': ['A', 'B', 'C', 'A', 'B', 'A', 'C'],
    'valor': [1, 2, 3, 2, 3, 4, 5]
})

df2 = pd.DataFrame({
    'nsu': ['A', 'B', 'D'],
    'valor_nsu': [4, 5, 6]
})
# %%
unificado = pd.merge(df1, df2, on='chave', how='outer',
                     suffixes=('_esquerda', '_direita'))
# %%
unificado = pd.concat([df1, df2]).reset_index()
unificado
# %%
dados = []

for arquivos in os.listdir(r''):
    df = pd.read_excel(arquivos)
    dados.append(df)

concatenado = pd.concat(dados, ignore_index=True)

# %%
df1['valor'].nunique()
df1['valor'].unique()
# %%

# %%

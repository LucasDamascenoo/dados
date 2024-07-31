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
df_user = {
    'id': [1, 2, 3, 4],
    'nome': ['lucas', 'bruce', 'tati', 'wayne'],
    'idade': [31, 32, 33, 35]
}
df_user = pd.DataFrame(df_user)
df_user
# %%
df_transacao = {
    'id_user': [1, 1, 1, 2, 3, 3, 5],
    'vl': [432, 532, 123, 6, 4, 87, 10],
    'qtProdutos': [2, 1, 3, 6, 10, 2, 7]
}
df_transacao = pd.DataFrame(df_transacao)
# %%

df_transacao.merge(df_user,
                   how="outer",
                   left_on="id_user",
                   right_on="id"
                   )

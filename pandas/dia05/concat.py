# %%
import pandas as pd
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
    'id_user': [5, 6, 7, 8, 3, 3, 5],
    'vl': [432, 532, 123, 6, 4, 87, 10],
    'qtProdutos': [2, 1, 3, 6, 10, 2, 7]
}
df_transacao = pd.DataFrame(df_transacao)

# %%

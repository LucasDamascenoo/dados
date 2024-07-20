# %%
import pandas as pd
# %%

df1 = pd.DataFrame({
    'chave': ['A', 'B', 'C'],
    'valor': [1, 2, 3]
})

df2 = pd.DataFrame({
    'chave': ['A', 'B', 'D'],
    'valor': [4, 5, 6]
})
# %%
unificado = pd.merge(df1, df2, on='chave', how='outer',
                     suffixes=('_esquerda', '_direita'))
# %%

# %%


# %%

# %%

chave	valor_esquerda	valor_direita
0	A	1.0	4.0
1	B	2.0	5.0
2	C	3.0	NaN
3	D	NaN	6.0

# %%

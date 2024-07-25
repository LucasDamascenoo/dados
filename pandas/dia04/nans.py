#%%
import pandas as pd
import numpy as np
# %%
data = {'nome':['Bruce','Lucas','Tati','Dona Lucia'],
        'idade':[7,29,np.nan,np.nan],
        'renda': [180,4500,np.nan,np.nan]}
# %%
df = pd.DataFrame(data)

# %%
df['idade'].isna().value_counts()
df['idade'].isna().sum()
df.isna().sum() # verifica quantos na existem em cada coluna do meu dataframe

# %%
# como descobrir a taxa de nas
df['idade'].mean()
# %%
# como preencher os valores nan por outro valor 
df.fillna({
    'idade':0,
    'renda': "N informado"
})
# %%
# como remover valores(linhas) nan
df2 = df.dropna(subset=["nome", "renda"], how="any")
df2
# %%
#dropando colunas
df3 = df.dropna(axis=1, how="all")
df3
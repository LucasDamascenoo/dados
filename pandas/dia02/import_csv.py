# %%
import pandas as pd
# %%
origem = pd.read_csv("../data/customers.csv", sep=';')

origem.head()

# %%
origem.info(memory_usage="deep")
# %%
origem.shape
# %%
origem.describe()
# %%
origem["Points"].astype(int)

# %%
condicao = origem['Points'] > 1000
origem[condicao]
# %%
maximo = origem['Points'].max()
condicao = origem['Points'] == maximo
origem[condicao]
# %%
origem[origem['Points'] == origem['Points'].max()]
# %%
cond = (origem['Points'] >= 1000) & (origem['Points'] <= 2000)
# %%
origem[['Name', 'UUID']]
# %%
colunas = origem.columns.tolist()
colunas.sort()

origem = origem[colunas]
origem
# %%
# renomear colunas
origem = origem.rename(columns={"Name": "Nome", "Points": "Pontos"})
origem
# %%
origem.rename(columns={"UUID": 'ID'}, inplace=True)
origem

# %%

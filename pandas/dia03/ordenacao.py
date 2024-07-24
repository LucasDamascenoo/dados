# %%
import pandas as pd

# %%
df = pd.read_csv('../data/customers.csv', delimiter=';')
df
# %%
# orndenando os pontos e nomes, um por descrecente e outra crescente
df = df.sort_values(by=['Points', 'Name'], ascending=[False, True]).rename(
    columns={'Name': 'Nome', 'Points': 'Pontos'}).reset_index()

# %%
df

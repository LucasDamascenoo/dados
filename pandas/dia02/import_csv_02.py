# %%
import pandas as pd

# %%

# %%
df = pd.read_csv('../data/products.csv',
                 sep=';',
                 # header=None,
                 names=["id", 'Name', 'Description'])
df
# %%
# %%
df = df.rename(columns={'Name': 'Nome', 'Description': 'Descrição'})
df
# %%

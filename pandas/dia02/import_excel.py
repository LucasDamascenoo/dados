# %%
import pandas as pd
# %%
df = pd.read_excel('../data/transactions.xlsx')
df

# %%
df.shape
# %%
df.head()
# %%
colunas = ['UUID', 'Points', 'IdCustomer', 'DtTransaction']
df = df[colunas]
df
# %%

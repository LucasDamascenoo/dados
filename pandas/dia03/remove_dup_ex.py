# %%
import pandas as pd
import openpyxl
# %%
df = pd.read_excel('../data/transactions.xlsx')

# %%
# ultima transacao de cada id costumer
df = df.sort_values(by='DtTransaction', ascending=True).drop_duplicates(
    subset=['IdCustomer'], keep="last")
df

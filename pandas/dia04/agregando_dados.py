# %%
import pandas as pd
import datetime
# %%
df = pd.read_excel('../data/transactions.xlsx')
df.groupby('IdCustomer').agg({
    'Points':'sum'
}).sort_values(by='Points',ascending=False)


# %%
def recencia(x):
    diff = datetime.datetime.now() - x.max()
    return  diff.days
df.groupby('IdCustomer').agg({
  'Points':'sum',
   'UUID':'count',
   'DtTransaction': ['max',recencia]

}).rename(columns={'Points':'Valor',
                   'UUID':'Frequencia',
                   'DtTransaction':'Ultima_Data'
                   }).reset_index()



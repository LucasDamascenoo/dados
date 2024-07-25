# %%
import pandas as pd
# %%
df = pd.read_excel('../data/transactions.xlsx')
df.groupby('IdCustomer').agg({
    'Points':'sum'
}).sort_values(by='Points',ascending=False)
# %%
df.groupby('IdCustomer').agg({
  'Points':'sum',
   'UUID':'count',
   'DtTransaction': 'max'

}).rename(columns={'Points':'Valor',
                   'UUID':'Frequencia',
                   'DtTransaction':'Ultima_Data'}).reset_index()
                   
# %%
 
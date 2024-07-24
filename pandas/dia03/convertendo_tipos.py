# %%
import pandas as pd
# %%
df = pd.read_csv('../data/customers.csv', delimiter=';')
df['Points'].astype('str')

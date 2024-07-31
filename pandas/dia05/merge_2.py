# %%
import pandas as pd
# %%
df_costumer = pd.read_csv('../data/customers.csv', delimiter=';')
df_transactions = pd.read_excel('../data/transactions.xlsx')
df_transactions_product = pd.read_parquet('../data/transactions_cart.parquet')
# %%
df_transactions_product.info()
# mergeando

# %%
df_merge = df_transactions.merge(df_costumer,
                                 how="inner",
                                 left_on='IdCustomer',
                                 right_on='UUID',
                                 suffixes=['_transacao', '_cliente']).merge(df_transactions_product,
                                                                            how='inner',
                                                                            left_on='UUID_transacao',
                                                                            right_on='IdTransaction')
# %%
df_merge
# %%

# %%

# %%

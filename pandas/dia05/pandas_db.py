# %%
import pandas as pd
import sqlalchemy
# %%
engine = sqlalchemy.create_engine("sqlite:///../data/database.db")
pd.read_sql_table("transactions_cart", engine)

# %%
# trabalhando com uma query

query = '''
select *
from customers
limit 100;'''
pd.read_sql_query(query, engine)

# %%

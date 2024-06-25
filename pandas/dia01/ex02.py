# %%
import pandas as pd
# %%
dados = {
    'nome': ["Bruce", "donaLucia", "Napoelao"],
    'idade': [10, 53, 120]
}
# %%
df = pd.DataFrame(dados)
df
# %%
# sumario
sumario_numericas = df.describe()
sumario_numericas

# %%
# sumarios não numericos
df['nome'].describe()
# %%
# media
df['idade'].mean()

# %%
# ultimo nome da coluna nome
df['nome'].iloc[-1]
# %%

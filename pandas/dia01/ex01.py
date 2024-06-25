# %%

import pandas as pd


# %%
dados = [10, 20, 42, 9, 12, 35, 24, 10, 8, 14, 21]
series = pd.Series(dados)
series
# %%
# média
media = series.mean()
media
# %%
# desvio Padrão
desvio = series.std()
desvio
# %%
maximo = series.max()
maximo
# %%

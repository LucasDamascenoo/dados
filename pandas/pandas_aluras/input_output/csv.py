# %%
# Salvando um dataFrame
import pandas as pd
# %%
data = {'Nome': ['João', 'Maria', 'Pedro', 'Ana'],
        'Idade': [25, 30, 35, 40],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Brasília']}

df = pd.DataFrame(data)

caminho = r'E:\teste\teste.csv'
df.to_csv(caminho, index=False)

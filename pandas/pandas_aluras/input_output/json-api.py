# %%
import pandas as pd
import requests
import json
# %%
dados_usuario = requests.get('https://jsonplaceholder.typicode.com/users')

resultado = json.loads(dados_usuario.text)
# %%
resultado_normalizado = pd.json_normalize(resultado, sep='_')
resultado_normalizado.to_excel('dados_usuarios.xlsx')

# %%

# %%

# %%

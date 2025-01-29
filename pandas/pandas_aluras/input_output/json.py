# %%

import pandas as pd
# %%
dados_brutos = pd.read_json('pacientes.json')
dados = pd.json_normalize(dados_brutos['Pacientes'])
dados.to_json('pacientes_normalizados.json')

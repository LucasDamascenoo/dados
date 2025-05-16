# %%

import random
import numpy as np
import matplotlib.pyplot as plt

# Simular base de dados com 300 clientes
parcerias = ["Nenhuma", "Empresa X", "Banco Y", "Associação Z"]
clientes = []

for i in range(300):
    parceria = random.choices(parcerias, weights=[0.6, 0.2, 0.15, 0.05])[0]

    # Definir mensalidade base
    mensalidade_base = random.uniform(35, 100)

    # Definir desconto conforme parceria
    if parceria == "Empresa X":
        desconto = 5.0
    elif parceria == "Banco Y":
        desconto = 10.0
    elif parceria == "Associação Z":
        desconto = 15.0
    else:
        desconto = 0.0

    # Simular outlier ocasional
    if random.random() < 0.02:
        mensalidade_base = random.uniform(150, 250)

    clientes.append({
        "id": i+1,
        "mensalidade": mensalidade_base,
        "desconto": desconto,
        "parceria": parceria
    })

# ----- 📊 Análise 1: Valor Médio de Mensalidade -----
mensalidades = [c["mensalidade"] for c in clientes]
media_geral = np.mean(mensalidades)

# Média por parceria
parcerias_unicas = list(set(parcerias))
media_parceria = {}
for p in parcerias_unicas:
    valores = [c["mensalidade"] for c in clientes if c["parceria"] == p]
    media_parceria[p] = np.mean(valores)

# Gráfico
plt.figure(figsize=(7, 5))
plt.bar(media_parceria.keys(), media_parceria.values(), color='skyblue')
plt.axhline(y=media_geral, color='r', linestyle='--',
            label=f'Média geral: R$ {media_geral:.2f}')
plt.title("Valor Médio de Mensalidade por Parceria")
plt.ylabel("R$ Mensalidade")
plt.legend()
plt.show()

# ----- 📊 Análise 2: Quantidade de Clientes com Desconto -----
com_desconto = len([c for c in clientes if c["desconto"] > 0])
sem_desconto = len(clientes) - com_desconto

# Gráfico
plt.figure(figsize=(6, 6))
plt.pie([com_desconto, sem_desconto],
        labels=["Com Desconto", "Sem Desconto"],
        autopct='%1.1f%%', colors=['lightgreen', 'lightcoral'])
plt.title("Percentual de Clientes com Desconto")
plt.show()

# ----- 📊 Análise 4: Receita Mensal Total -----
receita_bruta = sum(mensalidades)
receita_liquida = sum(c["mensalidade"] - c["desconto"] for c in clientes)

# Gráfico
plt.figure(figsize=(7, 5))
plt.bar(["Receita Bruta", "Receita Líquida"], [
        receita_bruta, receita_liquida], color=['orange', 'green'])
plt.title("Receita Mensal: Bruta vs Líquida")
plt.ylabel("R$ Total")
plt.show()

# ----- 📊 Análise 5: Receita por Parceria -----
receita_por_parceria = {}
for p in parcerias_unicas:
    total = sum(c["mensalidade"] - c["desconto"]
                for c in clientes if c["parceria"] == p)
    receita_por_parceria[p] = total

# Gráfico
plt.figure(figsize=(8, 5))
plt.bar(receita_por_parceria.keys(),
        receita_por_parceria.values(), color='blue')
plt.title("Receita Líquida por Parceria")
plt.ylabel("R$ Receita")
plt.show()

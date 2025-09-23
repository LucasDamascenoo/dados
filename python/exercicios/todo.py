import pandas as pd

# Exemplo de dataset
dados = {
    "cliente_id": [1, 2, 3, 1, 2, 4, 3, 5],
    "data_cobranca": [
        "2025-06-01", "2025-06-01", "2025-06-01",
        "2025-07-01", "2025-07-01", "2025-07-01",
        "2025-08-01", "2025-08-01"
    ],
    "valor_mensalidade": [100, 120, 150, 100, 120, 200, 150, 180]
}

df = pd.DataFrame(dados)
df["data_cobranca"] = pd.to_datetime(df["data_cobranca"])
df["mes"] = df["data_cobranca"].dt.to_period("M")

# Receita total por mês
receita_mes = df.groupby("mes")["valor_mensalidade"].sum()

# Clientes ativos por mês
clientes_mes = df.groupby("mes")["cliente_id"].nunique()

# Ticket médio
ticket_medio = receita_mes / clientes_mes

# Comparação mês a mês
comparacao = pd.DataFrame({
    "receita_total": receita_mes,
    "clientes_ativos": clientes_mes,
    "ticket_medio": ticket_medio
})

# Identificar novos clientes e churn
clientes_por_mes = df.groupby("mes")["cliente_id"].apply(set)

resultados = []
meses = list(clientes_por_mes.index)

for i in range(1, len(meses)):
    mes_atual = meses[i]
    mes_anterior = meses[i-1]

    novos = clientes_por_mes[mes_atual] - clientes_por_mes[mes_anterior]
    churn = clientes_por_mes[mes_anterior] - clientes_por_mes[mes_atual]

    resultados.append({
        "mes": mes_atual,
        "novos_clientes": len(novos),
        "clientes_churn": len(churn)
    })

churn_novos = pd.DataFrame(resultados)

print("KPIs mês a mês:")
print(comparacao)
print("\nNovos clientes e churn:")
print(churn_novos)

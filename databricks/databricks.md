# Databricks

---

## Unity Catalog

### O que é o Unity Catalog?

> [ ] anotar introdução

---

### Object Model — Hierarquia

Dentro do Databricks temos um sistema de "pastas" onde organizamos nossos dados.

```
Metastore
 └── Catalog
      └── Schema (database)
           ├── Tables
           ├── Views
           ├── Volumes
           └── Functions
```

---

### Metastore

Nível mais alto do Unity Catalog, onde controlamos os metadados da empresa.

- `permissoes` `localizacao de dados` `auditoria` `governanca`

> Existe um por região/conta. Criado pelo admin — transparente no dia a dia.

---

### Catalog

Nossa "gaveta" da organização, onde centralizamos todos os dados de acordo com o contexto/projeto.

- ex: `financeiro` `dev` `prod` `vendas`

```sql
CREATE CATALOG financeiro;

USE CATALOG financeiro;
```

---

### Schema

Onde criamos e agrupamos os objetos (tabelas, views, etc.) de acordo com cada catálogo.

- ex: `financeiro.raw` `financeiro.trusted` `financeiro.refined`

```sql
CREATE SCHEMA financeiro.raw;

USE SCHEMA financeiro.raw;
```

---

### Objetos dentro do Schema

#### Tables

Dados estruturados, como tabelas SQL. É o objeto mais comum do dia a dia.

- ex: `financeiro.raw.pedidos` `dev.vendas.produtos` `prod.vendas.items`

```sql
CREATE TABLE financeiro.raw.pedidos (
  id    INT,
  valor DOUBLE,
  data  DATE
);

SELECT * FROM financeiro.raw.pedidos;
```

---

#### Views

Consultas salvas que **não armazenam dados fisicamente**. Quando consultadas, executam a query por baixo automaticamente.

- ex: `financeiro.refined.pedidos_aprovados`

```sql
CREATE VIEW financeiro.refined.pedidos_aprovados AS
SELECT * FROM financeiro.trusted.pedidos
WHERE status = 'aprovado';

SELECT * FROM financeiro.refined.pedidos_aprovados;
```

---

#### Volumes

Onde guardamos arquivos físicos não estruturados — funciona como se fosse o S3, mas dentro do Unity Catalog.

- ex: `clientes.json` `vendas.csv` `foto_perfil.jpeg`

```python
df = spark.read.csv(
    "/Volumes/financeiro/raw/arquivos_brutos/vendas.csv",
    header=True
)
```

---

#### Functions

Funções reutilizáveis registradas no catálogo, disponíveis para qualquer pessoa do time usar via SQL ou Python.

- ex: `financeiro.raw.calcula_desconto(valor, pct)`

```sql
CREATE FUNCTION financeiro.raw.calcula_desconto(valor DOUBLE, pct DOUBLE)
RETURNS DOUBLE
RETURN valor - (valor * pct / 100);

-- usando
SELECT financeiro.raw.calcula_desconto(100.0, 10.0); -- retorna 90.0
```

---

### Three-Level Namespace

O padrão de acesso a qualquer objeto é sempre **3 níveis**:

```
catalog.schema.objeto
```

```sql
SELECT * FROM financeiro.raw.pedidos
SELECT * FROM dev.vendas.produtos
SELECT * FROM prod.vendas.items
```

> Isso garante que dois times podem ter uma tabela chamada `pedidos` sem conflito, pois cada uma vive num catalog/schema diferente.

---

### Controle de Acesso

> [ ] grants e permissões
> [ ] níveis de acesso (CATALOG, SCHEMA, TABLE)

---

### Data Lineage

> [ ] linhagem de dados
> [ ] como o Unity Catalog rastreia origem e transformações

---

### Hive Metastore vs Unity Catalog

> [ ] diferenças e quando cada um aparece
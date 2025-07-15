### A Filosofia: Aprender Fazendo

Para evitar a "paralisia por análise" dos video-tutoriais, nossa abordagem será:
* **Conceito e Aplicação Imediata:** Para cada nova tecnologia, você aprenderá o conceito fundamental e o aplicará em um pequeno exercício prático ou em uma parte de um projeto maior.
* **Projetos como Guia:** Os projetos não são algo que você fará "depois de aprender". Eles serão o principal motor do seu aprendizado.
* **Documentação é sua Amiga:** Aprenda a ler e a utilizar a documentação oficial das ferramentas. Esta é uma habilidade crucial em qualquer empresa de tecnologia.
* **Resolução de Problemas:** Encare os erros como parte do processo. A habilidade de depurar e encontrar soluções é o que diferencia um engenheiro de dados sênior.

---

### O Cronograma Detalhado

#### **Mês 1-2: A Fundação Sólida**

**Foco:** Dominar as ferramentas essenciais e os conceitos básicos de modelagem de dados.

| Semana | Tópicos de Estudo | Prática e Projetos | Dicas de Aprimoramento |
| :--- | :--- | :--- | :--- |
| **1-4** | **Python para Engenharia de Dados:**<br>- Estruturas de dados (listas, dicionários)<br>- Funções e módulos<br>- Manipulação de arquivos (CSV, JSON, Parquet)<br>- Ambientes virtuais e gerenciamento de dependências (venv, pip)<br>- Bibliotecas: Pandas, Requests | - **Mini-projeto:** Crie um script Python que consome uma API pública (ex: dados da FIPE, cotações de moedas), processa os dados (limpeza e transformação com Pandas) e os salva em diferentes formatos (CSV e Parquet). | - Foque na qualidade do código: use nomes de variáveis claros e adicione comentários.<br>- Comece a usar o Git para versionar seu mini-projeto. |
| **5-8** | **SQL do Básico ao Avançado:**<br>- `SELECT`, `FROM`, `WHERE`, `GROUP BY`, `HAVING`<br>- `JOINs` (INNER, LEFT, RIGHT, FULL OUTER)<br>- Subqueries e Common Table Expressions (CTEs)<br>- Window Functions (`ROW_NUMBER`, `LEAD`, `LAG`)<br>- Conceitos de Modelagem de Dados: Esquema Estrela (Star Schema) vs. Floco de Neve (Snowflake Schema), Normalização. | - **Prática Intensiva:** Resolva problemas de SQL em plataformas como HackerRank, LeetCode ou StrataScratch.<br>- **Mini-projeto:** Modele e crie um pequeno banco de dados relacional (usando PostgreSQL) para um e-commerce simples. Popule-o com dados fictícios e escreva queries complexas para responder a perguntas de negócio (ex: "quais os 5 produtos mais vendidos em cada categoria no último mês?"). | - Entenda os `EXPLAIN` plans para otimizar suas queries.<br>- Leia sobre os diferentes tipos de índices em bancos de dados. |

#### **Mês 3-4: Construindo Pipelines e Orquestração**

**Foco:** Aprender a mover e transformar dados em escala, e a automatizar esses processos.

| Semana | Tópicos de Estudo | Prática e Projetos | Dicas de Aprimoramento |
| :--- | :--- | :--- | :--- |
| **9-12** | **Cloud Computing (Escolha uma: AWS, GCP ou Azure):**<br>- **AWS:** S3 (armazenamento), EC2 (computação), IAM (permissões), RDS (banco de dados relacional)<br>- **Conceitos de Data Warehouse:** OLAP vs. OLTP, arquitetura de um DWH.<br>- **Ferramentas de ETL/ELT e Orquestração:**<br>  - **Apache Airflow:** Conceitos de DAGs, Operators, Sensors, XComs. | - **Início do Projeto 1 (Pipeline de Dados Batch):**<br>  - **Fase 1:** Configure a infraestrutura na nuvem (ex: um bucket no S3, uma instância de banco de dados no RDS).<br>  - **Fase 2:** Desenvolva scripts Python que extraem dados de múltiplas fontes (ex: a API do mês 1 e um arquivo CSV estático), transformam esses dados e os carregam no seu Data Warehouse na nuvem.<br>  - **Fase 3:** Crie uma DAG no Airflow para orquestrar e agendar a execução do seu pipeline diariamente. | - Foque em boas práticas no Airflow: crie DAGs idempotentes e modulares.<br>- Aprenda a usar a CLI da sua provedora de nuvem.<br>- Comece a pensar em logging e monitoramento para seu pipeline. |
| **13-16**| **Big Data Technologies (Batch):**<br>- **Apache Spark:** Arquitetura (Driver, Executors), RDDs, DataFrames e Spark SQL.<br>- **Ecossistema Hadoop:** Conceitos básicos de HDFS e MapReduce (entendimento conceitual é suficiente).<br>- **Data Lake:** Conceitos e diferenças para um Data Warehouse. | - **Projeto 1 (Evolução):**<br>  - Substitua o processamento com Pandas por PySpark. O objetivo é lidar com um volume de dados maior (você pode gerar dados sintéticos para simular isso).<br>  - Execute seu job Spark em um serviço gerenciado (ex: AWS EMR, Google Dataproc ou Azure Databricks).<br>  - Implemente logging e alertas básicos para sua DAG no Airflow. | - Leia sobre particionamento de dados em Spark e como isso afeta a performance.<br>- Comece a documentar seu projeto no GitHub com um `README.md` claro, explicando a arquitetura e como executá-lo. |

#### **Mês 5-6: Dados em Tempo Real e Preparação para o Mercado**

**Foco:** Trabalhar com dados em streaming e solidificar seu portfólio e habilidades para entrevistas.

| Semana | Tópicos de Estudo | Prática e Projetos | Dicas de Aprimoramento |
| :--- | :--- | :--- | :--- |
| **17-20**| **Streaming de Dados:**<br>- **Apache Kafka:** Conceitos de Tópicos, Partições, Producers e Consumers.<br>- **Spark Structured Streaming:** Processamento de dados em tempo real com Spark. | - **Início do Projeto 2 (Pipeline de Dados em Tempo Real):**<br>  - Crie um produtor de dados em Python que simula um stream de eventos (ex: cliques em um site, transações financeiras) e os envia para um tópico no Kafka.<br>  - Desenvolva uma aplicação com Spark Structured Streaming que consome esses dados do Kafka, realiza agregações em janela de tempo (ex: número de transações por minuto) e salva o resultado em um banco de dados ou em um sistema de arquivos. | - Estude sobre garantias de entrega de mensagens no Kafka (at-least-once, at-most-once, exactly-once).<br>- Explore como lidar com dados que chegam com atraso (late data) no Spark Streaming. |
| **21-24**| **Tópicos Avançados e Revisão:**<br>- **Infraestrutura como Código (IaC):** Básico de Terraform ou AWS CloudFormation.<br>- **CI/CD para Dados:** Conceitos de como automatizar testes e deploys de pipelines.<br>- **Qualidade e Governança de Dados:** Ferramentas como Great Expectations.<br>- Revisão de estruturas de dados e algoritmos (Data Structures & Algorithms - DSA). | - **Projeto 2 (Evolução):**<br>  - Use Terraform para provisionar sua infraestrutura de streaming (cluster Kafka, etc.).<br>  - Adicione testes de qualidade dos dados ao seu pipeline com uma ferramenta como Great Expectations.<br>- **Preparação para Entrevistas:**<br>  - Pratique problemas de codificação (Python e SQL) e system design focados em engenharia de dados.<br>  - Refine o `README.md` dos seus projetos no GitHub, adicionando diagramas de arquitetura. | - Contribua para um projeto open-source de engenharia de dados (mesmo que seja uma pequena correção na documentação).<br>- Participe de comunidades online (Reddit, Discord, etc.) para discutir soluções e aprender com outros engenheiros. |

---

### Projetos para um Portfólio de Destaque

#### **Projeto 1: Pipeline de Dados de E-commerce (Batch)**

* **Objetivo:** Construir um pipeline de dados de ponta a ponta que ingere, processa e armazena dados de um e-commerce para análise de negócio.
* **Fontes de Dados:**
    1.  API de um sistema de e-commerce (pode ser uma API pública ou uma que você mesmo crie com Flask/FastAPI).
    2.  Logs de cliques do site (arquivos JSON em um bucket S3).
    3.  Dados de produtos de um banco de dados relacional (PostgreSQL).
* **Tecnologias:**
    * **Ingestão:** Python, Requests.
    * **Armazenamento (Data Lake/Staging):** AWS S3 / Google Cloud Storage.
    * **Processamento:** Apache Spark rodando no AWS EMR / Google Dataproc.
    * **Orquestração:** Apache Airflow.
    * **Data Warehouse:** Amazon Redshift / Google BigQuery / Snowflake.
    * **Infraestrutura como Código:** Terraform (básico).
* **Entregáveis:**
    * Um repositório no GitHub com todo o código, DAGs do Airflow e arquivos de configuração do Terraform.
    * Um `README.md` detalhado com um diagrama da arquitetura, explicando o fluxo de dados e como executar o projeto.
    * Exemplos de queries SQL no Data Warehouse que demonstrem o valor dos dados processados.

#### **Projeto 2: Análise de Sentimento de Tweets em Tempo Real (Streaming)**

* **Objetivo:** Criar um sistema que coleta tweets sobre um determinado tópico em tempo real, analisa o sentimento de cada tweet e disponibiliza os resultados para visualização.
* **Fontes de Dados:** API do Twitter (ou uma simulação que gera dados em formato similar).
* **Tecnologias:**
    * **Coleta:** Python (com a biblioteca do Twitter).
    * **Fila de Mensagens:** Apache Kafka.
    * **Processamento em Tempo Real:** Spark Structured Streaming ou Apache Flink.
    * **Análise de Sentimento:** Uma biblioteca simples de NLP em Python.
    * **Armazenamento de Resultados:** Elasticsearch ou um banco de dados NoSQL como o MongoDB.
    * **Visualização (Opcional):** Um dashboard simples com Kibana, Grafana ou Streamlit.
* **Entregáveis:**
    * Repositório no GitHub com o código do produtor, da aplicação de streaming e as configurações.
    * `README.md` com diagrama da arquitetura de streaming, explicando o fluxo de eventos e os desafios (como processamento em janela de tempo).
# o que é a engenharia de dados?



# Pipelines de Dados

Pipelines de dados é um meio de mover dados de uma origem para um destino, como um data warehouse ou um data lake. Nesse caminho, os dados são tratados para que cheguem na ponta final da melhor forma possível.

- **Melhor definição**: Pipeline é uma etapa de processamento de dados (pega os dados da origem, limpa e carrega).

- Hoje existem ferramentas que automatizam pipelines.

- Pipelines é um conceito que podemos aplicar de diversas formas, como linguagens de programação.

- Cada pipeline possui etapas que fornecem uma saída (dados) que é a entrada para a próxima etapa.

**Componentes**: As pipelines sao compostas por 3 componentes fundamentais:

1. Origem dos dados
2. Processamento (limpeza/transformação)
3. Destino (Onde vamos colocar os dados)

# Pipelines vs ETL

- **ETL**: Processo tradicional de integração de dados que envolve extração, transformação e carregamento de dados em um data warehouse.
- **Pipelines de Dados**: Fluxo contínuo e automatizado de dados de uma origem para um destino, passando por várias etapas de processamento que podem incluir ETL, validação, enriquecimento, e análise em tempo real.


# Arquiteturas

# Coleta de Dados

Podemos fazer coletas de dados de diversas fontes como:

- Arquivos: parquet, csv, xlsx (sao oriundos de outros sistemas onde sao importados e algum tipo de arquivo e fazemos a insercao posteriormente).
- Apis: permite a extracao de dados de diversos sistemas, sao feitas atraves de requisicoes https.
- WebSites: sites existente que podemos fazer scraping (utilizado para raspar os dados e salvar em um csv,excel por exemplo) , crawlers (usados para criarmos uma lista de links).
- Tabelas: sao dados estruturados armazenados em sgbds onde podemos consultar, exportar.
- Iot : iots podemos trabalhar com diversos sensores, presenca, calor e uma infinidade.
- Pipelines de dados: o log de um pipeline de dados pode ser uma fonte de dados por exemplo.

## Apis

- 

- endpoint sao "pedaços" de uma api que tras informaçoes distintas

https://api/github.com/versions (versions é o endpoint)

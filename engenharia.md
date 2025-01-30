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

- Apis sao interfaces de programacao que como se fosse um'interprete' que padroniza e troca informacoes com diversos sistemas,usamos muito apis para buscarmos dados de diversas fontes.

Apis podem ser Rest (sao apis que utilizam procotocolo HTTP (get,put,delete)) para enviar e receber dados em formatos json,xml, e tambem existem Apis de streaming que permite a transmisao de dados em tempo real.

Temos Apis publicas(nao necessita autenticacao para usarmos) e privadas (e necessario autenticacao/tokem para acesso)

 **requisições**: requisições sao pedidos que fazemos para um servidor para que ele nos der informacoes ou execute uma determinada acao, mas mais comuns sao.

- Get: a requisicao mais utilizada e e responsavel por buscar inforcacoes no servidor.
- Post: utilizada para enviar informacoes para o servidor, como um novo usuario,dados de um form.
- Put: utilizada para substuicoes completas de informacoes no servidor
- Delete: Utilizada para deletar informacoes do servidor
- Patch: utilizada para atualizacoes particais

 **Status Code**: sempre que utilizamos uma requisicao, ela nos retorna um status code, informando se foi bem sucessida, deu algum erro ou falta alguma coisa.

- 2xx(sucesso) : indica que o servidor esta retornando as informacoes de forma correta

- 3xx(redirecionamento) : indica que o cliente deve realizar + alguma acao para que que tenha retorno das informacoes

- 4xx(erro do cliente) : informa erro por parte do cliente, como pagina nao encontrada

- 5xx(erro do servidor): informa que existe erros do lado do servidor.

**endpoint**:  Um endpoint é uma parte específica de uma URL de API que fornece informações distintas.

- www.restaurante.com → Domínio principal (não é necessariamente uma API).
- www.restaurante.com/api → Pode ser a base da API.
- www.restaurante.com/api/menu → Endpoint que retorna o cardápio.
- www.restaurante.com/api/pedidos → Endpoint que retorna pedidos feitos.
- https://api/github.com/versions → (versions é o endpoint)

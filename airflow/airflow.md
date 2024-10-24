# Airflow

Apache Airflow é uma plataforma de código aberto para criar, agendar e monitorar workflows programaticamente. Ele permite que você defina seus workflows como código, usando Python, o que facilita a criação, manutenção e monitoramento de pipelines de dados complexos.

## Principais Características

- **Orquestração de Workflows**: Airflow permite definir e gerenciar workflows complexos, garantindo que as tarefas sejam executadas na ordem correta e gerenciando dependências entre elas.
- **Definição de Workflows como Código**: Workflows são definidos como código Python, o que facilita a versionamento, teste e manutenção.
- **Agendamento**: Airflow permite agendar tarefas para serem executadas em intervalos regulares ou em horários específicos.
- **Monitoramento e Logging**: Airflow fornece uma interface web para monitorar a execução dos workflows, visualizar logs e depurar problemas.
- **Extensibilidade**: Airflow é altamente extensível, permitindo a criação de operadores personalizados e a integração com uma ampla variedade de sistemas e serviços.

## Componentes Principais

- **Interface Web**: A interface web do Airflow permite visualizar e monitorar a execução dos DAGs, além de fornecer acesso aos logs das tarefas.
- **Scheduler**: O Scheduler é responsável por agendar as tarefas para execução, de acordo com as dependências e horários definidos.
- **Executor**: O Executor é responsável por executar as tarefas agendadas.
- **Operadores**: Operadores sao modelos que define como as tasks serao executada,se eu quiser rodar um python utilizamos o operator PythonOperator: Executa uma função Python.
- **DAG (Directed Acyclic Graph)**: Um DAG é uma coleção de todas as tarefas que você deseja executar, organizadas de uma maneira que reflete suas dependências.

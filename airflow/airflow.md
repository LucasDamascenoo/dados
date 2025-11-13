# Airflow

Apache Airflow é uma plataforma de código aberto para criar, agendar e monitorar workflows programaticamente. Ele permite que você defina seus workflows como código, usando Python, o que facilita a criação, manutenção e monitoramento de pipelines de dados complexos.

## Principais Características

- **Orquestração de Workflows**: Airflow permite definir e gerenciar workflows complexos, garantindo que as tarefas sejam executadas na ordem correta e gerenciando dependências entre elas.
- **Definição de Workflows como Código**: Workflows são definidos como código Python, o que facilita a versionamento, teste e manutenção.
- **Agendamento**: Airflow permite agendar tarefas para serem executadas em intervalos regulares ou em horários específicos.
- **Monitoramento e Logging**: Airflow fornece uma interface web para monitorar a execução dos workflows, visualizar logs e depurar problemas.
- **Extensibilidade**: Airflow é altamente extensível, permitindo a criação de operadores personalizados e a integração com uma ampla variedade de sistemas e serviços.

## Componentes Principais

- **DAG (Directed Acyclic Graph)**: Um DAG é uma coleção de todas as tarefas que você deseja executar, organizadas de uma maneira que reflete suas dependências.
- **Interface Web**: A interface web do Airflow permite visualizar e monitorar a execução dos DAGs, além de fornecer acesso aos logs das tarefas.
- **Scheduler**: O Scheduler é responsável por agendar as tarefas para execução, de acordo com as dependências e horários definidos.
- **Executor**: O Executor é responsável por executar as tarefas agendadas.
- **Operadores**: Operadores sao modelos que define como as tasks serao executada,se eu quiser rodar um python utilizamos o operator PythonOperator: Executa uma função Python.


## Dags

- o conceito de uma dag e o conjunto de varias tarefas (tasks) que eh quebrar um processo em diversas etapas que no fim resulta em uma acao final.

**DAG - realizar provar**

TASK1 > definir tema da prova 
TASK2 > estudar por livros
TASK3 > estudar no yt
TASK4> realizar exercicios
TASK5> fazer a prova

### Parametros 'necessarios' para criar uma dag


 ```Python:

 @dag(start_date=datetime(2025,04,11),
      schedule='@daily',
      catchup = False,
      description = 'essa dag executa um etl referente a vendas',
      tags = ['vendas'],
      default_args = {'retries':1},
      dagrun_timeout=timedelta(minutes:20),
      max_consecutive_failed_dag_runs=2)

```
- **start_date:** data de inicio do agendamento da dag
- **schedule:** define a frequencia que a dag vai ser executada
- **catchup:**  Se True, executa execuções pendentes desde o start_date. Se False, só executa a partir do momento atual.
- **description:** Texto descritivo da DAG, aparece na UI do Airflow.
- **tags:** Lista de rótulos usados para categorizar a DAG na interface.
- **default_args:** Dicionário com configurações padrão aplicadas às tasks da DAG
- **dagrun_timeout:**  Tempo máximo que uma execução da DAG pode durar antes de ser interrompida.
- **max_consecutive_failed_dag_runs:** Número máximo de execuções consecutivas com falha antes de o Airflow pausar a DAG automaticamente









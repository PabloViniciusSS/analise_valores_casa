# Análise de Valores de Casas / House Value Analysis

Este projeto simula um cenário real de precificação imobiliária, com o objetivo de estimar o valor mediano de imóveis a partir de variáveis demográficas e geográficas extraídas do California Housing Dataset.  
This project simulates a real-world housing price prediction scenario, aiming to estimate the median house value based on demographic and geographic features from the California Housing Dataset.

A solução foi desenvolvida como um pipeline completo de Machine Learning, para o aprimoramento pessoal e profissional, com o intuito de demonstrar o conhecimento adquirido e as habilidades que um engenheiro hoje necessitaria.  
The solution was developed as a complete Machine Learning pipeline for personal and professional growth, demonstrating the knowledge acquired and the skills expected from a modern engineer.

O projeto contempla / The project includes:

- Formulação do problema e definição da variável alvo / Problem formulation and target variable definition
- Análise exploratória de dados (EDA) / Exploratory Data Analysis (EDA)
- Engenharia e transformação de atributos / Feature engineering and transformation
- Tratamento de valores ausentes / Handling missing values
- Normalização dos dados / Data normalization
- Transformação binária de dados / Binary data transformation
- Construção de pipelines com separação treino/teste / Pipeline construction with train/test split
- Treinamento e comparação de múltiplos modelos / Training and comparison of multiple models
- Avaliação com métricas como RMSE e MAE / Evaluation using metrics such as RMSE and MAE
- Validação cruzada e ajuste de hiperparâmetros / Cross-validation and hyperparameter tuning
- Estruturação do projeto para escalabilidade e versionamento / Project structuring for scalability and version control

## Definição do Problema / Problem Definition

### Objetivo de negócio / Business Objective

Desenvolver um modelo capaz de prever o valor mediano de imóveis por distritos. A predição será utilizada por um sistema downstream responsável por decidir se uma determinada região deve ou não receber um investimento imobiliário.  
O impacto do modelo é direto na receita da empresa, pois decisões incorretas podem gerar perdas financeiras.  

Develop a model capable of predicting the median house value by district. The prediction will be used by a downstream system responsible for deciding whether a certain region should receive a real estate investment.  
The model has a direct impact on company revenue, as incorrect decisions can generate financial losses.

### Solução Atual / Current Solution

Atualmente, a empresa utiliza profissionais para definir manualmente essa estimativa, sem considerar a mediana dos preços de habitação.  
O problema desse modelo manual é que ele é demorado e apresenta uma taxa média de erro de 15%, que será nosso baseline de comparação. Portanto, o modelo precisa performar melhor que esse percentual.  

Currently, the company relies on professionals to manually define these estimates, without considering the median housing prices.  
The problem with this manual approach is that it is time-consuming and has an average error rate of 15%, which will serve as our baseline for comparison. Therefore, the model must outperform this percentage.

### Enquadramento do Modelo / Model Framing

- É um modelo com dados supervisionados, pois os dados têm uma saída conhecida (target).  
- Trata-se de uma tarefa de regressão multivariada, pois existem múltiplas variáveis preditoras.  
- Será utilizado batch learning, pois os dados estão em um bloco fixo, sem fluxo contínuo e sem necessidade de atualização em tempo real.  

- This is a supervised learning problem, as the data has a known output (target).  
- It is a multivariate regression task, as there are multiple predictor variables.  
- Batch learning will be used, as the data comes in a fixed block, without continuous flow and without real-time update requirements.

## Procedimentos Iniciais de Tratamento de Dados / Initial Data Processing Procedures

O sistema foi estruturado para ser escalável, com persistência de dados em cada etapa.  
Neste projeto, a prioridade inicial é a ingestão e persistência de dados brutos (RAW), seguida de limpeza e normalização para posterior modelagem de Machine Learning.  
A cada etapa (RAW, CLEAN, FEATURE) serão realizadas operações e armazenamentos no banco para análises futuras.  

The system is structured to be scalable, with data persistence at every stage.  
In this project, the initial priority is the ingestion and persistence of raw data (RAW), followed by cleaning and normalization for subsequent Machine Learning modeling.  
At each stage (RAW, CLEAN, FEATURE), operations and database storage are performed for future analyses.

## Status do Projeto / Project Status

Atualmente o projeto está na **fase RAW**, com os seguintes pontos concluídos:  

- Ingestão de dados brutos (`housing.csv`) no banco de dados  
- Criação do schema e tabela RAW (`raw_housing`)  
- Configuração do core do projeto (logger, settings e database)  
- Contrato (`contract.py`) e models para organização dos dados  

Planned next steps / Próximas etapas planejadas:

- **CLEAN**: limpeza e tratamento de inconsistências nos dados / cleaning and handling data inconsistencies  
- **FEATURE**: engenharia de features / feature engineering  
- **Modelagem**: construção e avaliação de modelos de regressão / building and evaluating regression models  
- **Validação**: métricas e ajuste de hiperparâmetros / metrics evaluation and hyperparameter tuning

## Estrutura das pastas / Folder Structure

A estrutura das pastas será a seguinte / The folder structure is as follows:

```text
analise_valores_casa/
│
├── data/
│   └── raw/
│       └── housing.csv          # Dataset original usado para ingestão / Original dataset used for ingestion
│
├── sql/
│   └── ddl/
│       ├── raw/                 # Scripts DDL para criação da tabela raw_housing / DDL scripts for raw_housing table
│       │   └── 001_create_raw_housing.sql
│       ├── clean/               # Scripts DDL para tabelas intermediárias limpas / DDL scripts for cleaned intermediate tables
│       └── feature/             # Scripts DDL para tabelas de features derivadas / DDL scripts for derived feature tables
│
├── src/
│   ├── core/
│   │   ├── settings.py          # Configurações do projeto (paths, DB, environment) / Project settings
│   │   ├── database.py          # Conexão e sessão com o banco de dados / Database connection and session
│   │   └── logger.py            # Logger central do pipeline / Central pipeline logger
│   │
│   ├── layers/
│   │   ├── raw/                 # Camada RAW / RAW layer
│   │   │   ├── contract.py      # Definição do schema/contrato de dados / Data schema/contract definition
│   │   │   ├── ingestion.py     # Função de ingestão para raw_housing / Ingestion function for raw_housing
│   │   │   ├── pipeline.py      # Pipeline de ingestão RAW / RAW ingestion pipeline
│   │   │   └── models.py        # Modelos iniciais do RAW / Initial RAW models
│   │   │
│   │   ├── clean/               # Camada CLEAN (planejada) / CLEAN layer (planned)
│   │   │   └── pipeline.py      # Pipeline de limpeza / Cleaning pipeline
│   │   │
│   │   └── feature/             # Camada FEATURE (planejada) / FEATURE layer (planned)
│   │       └── pipeline.py      # Pipeline de engenharia de features / Feature engineering pipeline
│   │
│   ├── pipelines/
│   │   └── main_pipeline.py     # Orquestrador dos pipelines (opcional) / Pipelines orchestrator (optional)
│   │
│   └── main.py                  # Entry point do projeto / Project entry point
│
├── models/                      # Modelos treinados (quando aplicável) / Trained models (when applicable)
│
├── reports/                     # Relatórios e logs gerados / Generated reports and logs
│
├── notebooks/                   # Notebooks exploratórios ou testes / Exploratory notebooks or tests
│
├── tests/                       # Testes unitários e de integração / Unit and integration tests
│
├── requirements.txt             # Dependências Python / Python dependencies
├── README.md                     # Documentação do projeto / Project documentation
├── docker-compose.yml            # Configuração Docker Compose / Docker Compose configuration
└── Dockerfile                    # Imagem do container da aplicação / Application container image

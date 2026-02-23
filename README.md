# Análise de Valores de Casas ↔ House Value Analysis

| Português | English |
|-----------|---------|
| Este projeto simula um cenário real de precificação imobiliária, com o objetivo de estimar o valor mediano de imóveis a partir de variáveis demográficas e geográficas do California Housing Dataset. | This project simulates a real-world housing price prediction scenario, aiming to estimate the median house value based on demographic and geographic features from the California Housing Dataset. |
| A solução foi desenvolvida como um pipeline completo de Machine Learning, demonstrando conhecimento e habilidades práticas de engenharia de dados e ML. | The solution was developed as a complete Machine Learning pipeline, demonstrating practical knowledge and skills in data engineering and ML. |

## Funcionalidades / Features

| Português | English |
|-----------|---------|
| Formulação do problema e definição da variável alvo | Problem formulation and target variable definition |
| Análise exploratória de dados (EDA) | Exploratory Data Analysis (EDA) |
| Engenharia e transformação de atributos | Feature engineering and transformation |
| Tratamento de valores ausentes | Handling missing values |
| Normalização dos dados | Data normalization |
| Transformação binária de dados | Binary data transformation |
| Construção de pipelines com separação treino/teste | Pipeline construction with train/test split |
| Treinamento e comparação de múltiplos modelos | Training and comparison of multiple models |
| Avaliação com métricas como RMSE e MAE | Evaluation using metrics such as RMSE and MAE |
| Validação cruzada e ajuste de hiperparâmetros | Cross-validation and hyperparameter tuning |
| Estruturação do projeto para escalabilidade e versionamento | Project structuring for scalability and version control |

## Objetivo de Negócio / Business Objective

| Português | English |
|-----------|---------|
| Desenvolver um modelo capaz de prever o valor mediano de imóveis por distritos. A predição será usada para decisões de investimento imobiliário. | Develop a model capable of predicting the median house value by district. The prediction will be used for real estate investment decisions. |
| Impacto direto na receita da empresa, decisões incorretas podem gerar perdas financeiras. | Direct impact on company revenue, incorrect decisions may cause financial losses. |

## Status do Projeto / Project Status

| Português | English |
|-----------|---------|
| Atualmente na **fase RAW**, com: | Currently in the **RAW stage**, with: |
| - Ingestão de dados brutos (`housing.csv`) no banco de dados | - Raw data ingestion (`housing.csv`) into the database |
| - Criação do schema e tabela RAW (`raw_housing`) | - RAW schema and table (`raw_housing`) creation |
| - Configuração do core (logger, settings, database) | - Core configuration (logger, settings, database) |
| - Contrato (`contract.py`) e models para organização dos dados | - Contract (`contract.py`) and models for structured data handling |

Próximas etapas / Next steps:

| Português | English |
|-----------|---------|
| **CLEAN**: limpeza e tratamento de inconsistências | **CLEAN**: data cleaning and handling inconsistencies |
| **FEATURE**: engenharia de features | **FEATURE**: feature engineering |
| **Modelagem**: construção e avaliação de modelos de regressão | **Modeling**: building and evaluating regression models |
| **Validação**: métricas e ajuste de hiperparâmetros | **Validation**: metrics evaluation and hyperparameter tuning |

## Estrutura das Pastas / Folder Structure

| Português | English |
|-----------|---------|
| data/raw/housing.csv | data/raw/housing.csv |
| sql/ddl/raw/001_create_raw_housing.sql | sql/ddl/raw/001_create_raw_housing.sql |
| src/core/settings.py, database.py, logger.py | src/core/settings.py, database.py, logger.py |
| src/layers/raw/contract.py, ingestion.py, pipeline.py, models.py | src/layers/raw/contract.py, ingestion.py, pipeline.py, models.py |
| src/layers/clean/pipeline.py | src/layers/clean/pipeline.py |
| src/layers/feature/pipeline.py | src/layers/feature/pipeline.py |
| src/pipelines/main_pipeline.py | src/pipelines/main_pipeline.py |
| src/main.py | src/main.py |
| models/ | models/ |
| reports/ | reports/ |
| notebooks/ | notebooks/ |
| tests/ | tests/ |
| requirements.txt, Dockerfile, docker-compose.yml | requirements.txt, Dockerfile, docker-compose.yml |

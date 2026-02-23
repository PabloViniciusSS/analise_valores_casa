# Análise de Valores de Casas

Este projeto simula um cenário real de precificação imobiliária, com o objetivo de estimar o valor mediano de imóveis a partir de variáveis demográficas e geográficas extraídas do California Housing Dataset.

A solução foi desenvolvida como um pipeline completo de Machine Learning, para o aprimoramento pessoal e profissional, com o intuito de demonstrar o conhecimento adquirido e as habilidades que um engenheiro hoje necessitaria.

O projeto contempla:

- Formulação do problema e definição da variável alvo
- Análise exploratória de dados (EDA)
- Engenharia e transformação de atributos
- Tratamento de valores ausentes
- Normalização dos dados
- Transformação binária de dados
- Construção de pipelines com separação treino/teste
- Treinamento e comparação de múltiplos modelos
- Avaliação com métricas como RMSE e MAE
- Validação cruzada e ajuste de hiperparâmetros
- Estruturação do projeto para escalabilidade e versionamento

## Definição do Problema

### Objetivo de negócio

Desenvolver um modelo capaz de prever o valor mediano de imóveis por distritos. A predição será utilizada por um sistema downstream responsável por decidir se uma determinada região deve ou não receber um investimento imobiliário.  
O impacto do modelo é direto na receita da empresa, pois decisões incorretas podem gerar perdas financeiras.

### Solução Atual

Atualmente, a empresa utiliza profissionais para definir manualmente essa estimativa, sem considerar a mediana dos preços de habitação.  
O problema desse modelo manual é que ele é demorado e apresenta uma taxa média de erro de 15%, que será nosso baseline de comparação. Portanto, o modelo precisa performar melhor que esse percentual.

### Enquadramento do Modelo

- É um modelo com dados supervisionados, pois os dados têm uma saída conhecida (target).  
- Trata-se de uma tarefa de regressão multivariada, pois existem múltiplas variáveis preditoras.  
- Será utilizado batch learning, pois os dados estão em um bloco fixo, sem fluxo contínuo e sem necessidade de atualização em tempo real.

## Procedimentos Iniciais de Tratamento de Dados 

O sistema foi estruturado para ser escalável, com persistência de dados em cada etapa.  
Neste projeto, a prioridade inicial é a ingestão e persistência de dados brutos (RAW), seguida de limpeza e normalização para posterior modelagem de Machine Learning.  
A cada etapa (RAW, CLEAN, FEATURE) serão realizadas operações e armazenamentos no banco para análises futuras.

## Status do Projeto

Atualmente o projeto está na **fase RAW**, com os seguintes pontos concluídos:  
- Ingestão de dados brutos (`housing.csv`) no banco de dados  
- Criação do schema e tabela RAW (`raw_housing`)  
- Configuração do core do projeto (logger, settings e database)  
- Contrato (`contract.py`) e models para organização dos dados  

Próximas etapas planejadas:  
- **CLEAN**: limpeza e tratamento de inconsistências nos dados  
- **FEATURE**: engenharia de features  
- **Modelagem**: construção e avaliação de modelos de regressão  
- **Validação**: métricas e ajuste de hiperparâmetros

## Estrutura das pastas

A estrutura das pastas será a seguinte:

```text
analise_valores_casa/
│
├── data/
│   └── raw/
│       └── housing.csv          # Dataset original usado para ingestão
│
├── sql/
│   └── ddl/
│       ├── raw/                 # Scripts DDL para criação da tabela raw_housing
│       │   └── 001_create_raw_housing.sql
│       ├── clean/               # Scripts DDL para tabelas intermediárias limpas
│       └── feature/             # Scripts DDL para tabelas de features derivadas
│
├── src/
│   ├── core/
│   │   ├── settings.py          # Configurações do projeto (paths, DB, environment)
│   │   ├── database.py          # Conexão e sessão com o banco de dados
│   │   └── logger.py            # Logger central do pipeline
│   │
│   ├── layers/
│   │   ├── raw/                 # Camada RAW
│   │   │   ├── contract.py      # Definição do schema/contrato de dados
│   │   │   ├── ingestion.py     # Função de ingestão para raw_housing
│   │   │   ├── pipeline.py      # Pipeline de ingestão RAW
│   │   │   └── models.py        # Modelos iniciais do RAW
│   │   │
│   │   ├── clean/               # Camada CLEAN (planejada)
│   │   │   └── pipeline.py      # Pipeline de limpeza
│   │   │
│   │   └── feature/             # Camada FEATURE (planejada)
│   │       └── pipeline.py      # Pipeline de engenharia de features
│   │
│   ├── pipelines/
│   │   └── main_pipeline.py     # Orquestrador dos pipelines (opcional)
│   │
│   └── main.py                  # Entry point do projeto
│
├── models/                      # Modelos treinados (quando aplicável)
│
├── reports/                     # Relatórios e logs gerados
│
├── notebooks/                   # Notebooks exploratórios ou testes
│
├── tests/                       # Testes unitários e de integração
│
├── requirements.txt             # Dependências Python
├── README.md                     # Documentação do projeto
├── docker-compose.yml            # Configuração Docker Compose
└── Dockerfile                    # Imagem do container da aplicação
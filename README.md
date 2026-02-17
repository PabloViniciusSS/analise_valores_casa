# Análise de Valores de Casas

Este projeto simula um cenário real de precificação imobiliária, com o objetivo de estimar o valor mediano de imóveis a partir de variáveis demográficas e geográficas extraídas do California Housing Dataset.

A solução foi desenvolvida como um pipeline completo de Machine Learning, para o aprimoramento pessoal e profissional, com o intuito de demostrar o conhecimento addquirido e as habilidades que um engenheiro hoje necessitaria.

O projeto contempla:

- Formulação do problema e definição da variável alvo
- Análise exploratória de dados (EDA)
- Engenharia e transformação de atributos
- Tratamento de valores ausentes
- Construção de pipelines com separação treino/teste
- Treinamento e comparação de múltiplos modelos
- Avaliação com métricas como RMSE e MAE
- Validação cruzada e ajuste de hiperparâmetros
- Estruturação do projeto para escalabilidade e versionamento

## Definição do Problema

### Objetivo de negocio

Desenvolver um modelo de capaz prever o valor mediano de imóveis por distritos. A predição será utilizada por um sistema downstream responsavel por decidir se uma determinadar região deve ou não receber um investimento imobiliarios.
O impacto no modelo é direto na receita da empresa, pois, decisões incorretas podem impactar perdas financeiras.

### Solução Atual

Atualmente a empresa utiliza profissionais para definir manualmente essa estimativa, eles não utilizam a mediana dos preços de habitação, o problema desse modelo é que demorado e as estimativas não sao tão grandes, e a uma taxa média de erro de 15%, que seria nosso baseline de comparação, logo, nosso modelo tem que performar melhor que esses 15%.

### Enquadramento do ModeloProblemas

 - É um modelos com dados supervisionados, pois, os dados tem uma saída proposta, isto é um target.
 - Uma tarefa de regressão multivariada, pois, existe multiplas variás preditoras.
 - No caso vamos usar um lote de dados ou batch learning, pois, esses dados estão em um bloco fixo, sem um fluxo continuo de dados e uma necessidade de atualização em tempo real.






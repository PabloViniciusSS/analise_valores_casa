FROM python:3.11-slim
# Instala dependências do sistema para o Postgres
RUN apt-get update && apt-get install -y libpq-dev gcc && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia apenas o necessário primeiro (otimização de cache)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do projeto
COPY . .

# Mantém o container vivo para você entrar e rodar os scripts
CMD ["tail", "-f", "/dev/null"]
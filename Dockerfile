# Usa uma imagem base Python leve e específica
FROM python:3.11-slim

# Define o diretório de trabalho dentro do contêiner
WORKDIR /app

# Não queremos o .venv nem o banco de dados
# O Docker ignora o .gitignore, mas é bom ter um .dockerignore para arquivos grandes.

# Copia e instala as dependências primeiro para aproveitar o cache do Docker
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante dos arquivos da aplicação (main.py, models.py, schemas.py, etc.)
COPY . .

# Expõe a porta que o Uvicorn vai usar
EXPOSE 8000

# Comando para iniciar o servidor Uvicorn (Host 0.0.0.0 é obrigatório no Docker)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
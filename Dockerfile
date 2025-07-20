# Dockerfile
FROM python:3.11-slim

# Define diretório de trabalho
WORKDIR /app

# Copia os arquivos necessários
COPY . .

# Instala as dependências
RUN pip install --no-cache-dir fastapi uvicorn

# Expõe a porta padrão da aplicação
EXPOSE 8000

# Comando para iniciar a aplicação
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

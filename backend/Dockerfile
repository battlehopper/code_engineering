# Usar uma imagem Python oficial como imagem base
FROM python:3.9-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o arquivo de dependências
COPY requirements.txt requirements.txt

# Instalar as dependências
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o restante do código da aplicação
COPY . .

# Expor a porta em que o gunicorn irá rodar
EXPOSE 5000

# Comando para iniciar a aplicação com Gunicorn
# Isso fornece um servidor de produção robusto.
# O 'app:app' refere-se ao arquivo 'app.py' e à variável 'app' dentro dele.
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]

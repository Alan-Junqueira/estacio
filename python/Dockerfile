# Use uma imagem base do Python
FROM python

# Define o diretório de trabalho no contêiner
WORKDIR /app

# Copie os arquivos de código-fonte para o contêiner
COPY . /app

# Instale as dependências (se necessário)
# RUN pip install -r requirements.txt

# Mantenha o contêiner ativo com um loop infinito
CMD ["tail", "-f", "/dev/null"]
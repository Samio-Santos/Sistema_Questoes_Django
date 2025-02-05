# Usa uma imagem base estável do Python
FROM python:3.8-buster

# Configurações para evitar criação de arquivos .pyc e buffer de saída
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Define o diretório de trabalho dentro do container
WORKDIR /app

# Copia apenas o arquivo de dependências primeiro (melhora o cache)
COPY requirements.txt /app/requirements.txt

# Instala as dependências do projeto
RUN pip install --no-cache-dir -r requirements.txt

# Agora copia o restante dos arquivos do projeto
COPY . /app

# Coleta arquivos estáticos (garantindo que a pasta STATIC_ROOT tenha os arquivos necessários)
RUN python manage.py collectstatic --noinput

# Executa as migrações antes de iniciar o servidor
RUN python manage.py migrate --noinput

# Expõe a porta onde o Gunicorn vai rodar
EXPOSE 8000

# Comando para iniciar o Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "quiz.wsgi:application"]

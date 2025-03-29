#!/bin/bash

# Para o script em caso de erro
set -e  

# Força o reset das alterações locais
git reset --hard HEAD
git clean -fd

# Atualiza o código
git pull origin main

# Constrói e recria os containers
docker-compose down
docker-compose build
docker-compose up -d

# Aplica migrações dentro do container Django (removido -it)
docker exec sistema_container python manage.py makemigrations
docker exec sistema_container python manage.py migrate

# Coleta arquivos estáticos (removido -it)
docker exec sistema_container python manage.py collectstatic --noinput

# Reinicia os containers
docker-compose restart
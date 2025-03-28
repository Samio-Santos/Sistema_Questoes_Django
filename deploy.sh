#!/bin/bash

# Para o script em caso de erro
set -e  

# Atualiza o código
git pull origin main

# Constrói e recria os containers
docker-compose down
docker-compose build
docker-compose up -d

# Aplica migrações dentro do container Django
docker exec -it sistema_container python manage.py migrate

# Coleta arquivos estáticos
docker exec -it sistema_container python manage.py collectstatic --noinput

# Reinicia os containers
docker-compose restart

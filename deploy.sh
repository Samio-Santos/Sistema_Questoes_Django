#!/bin/bash

# Para o script em caso de erro
set -e  

# Verifica se há alterações locais no deploy.sh e realiza o commit ou stash, se necessário

# Se o deploy.sh foi alterado localmente, comita ou faz o stash das alterações
git diff --exit-code deploy.sh || {
    echo "Alterações locais encontradas em deploy.sh, commit ou stash necessário."

    # Comitar as mudanças no deploy.sh
    git add deploy.sh
    git commit -m "Alterações locais em deploy.sh antes do pull"

    # Alternativa: se preferir guardar temporariamente as alterações
    # git stash
}

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

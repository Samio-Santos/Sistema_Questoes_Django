# from django.contrib.auth.models import User
# from django.shortcuts import redirect
from django.contrib import messages


# def check_email_exists(request, backend, details, uid, user, *args, **kwargs):
#     email = details.get('email')
#     provider = backend.name

#     social = backend.strategy.storage.user.get_social_auth(provider, uid)
#     email_exists = User.objects.filter(email=email).exists()


# Exibe mensagem quando o usuario se loga com alguma rede social
def sucesso(request, backend, details, uid, user, *args, **kwargs):
    messages.success(request, f'Seja bem-vindo {user.first_name} {user.last_name}!')

from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import CostumerUser


def login(request):
    if request.method != 'POST':
        return render(request, 'accounts_templates/login.html')

    usuario = request.POST.get('user')
    senha = request.POST.get('password')

    user = auth.authenticate(request, username=usuario, password=senha)
    modelUser = get_user_model()
    try:
        # Verifica se o usuario fez cadastro com alguma rede social
        rede_social = modelUser.objects.get(email=usuario)
        # Verifica se o username é diferente do email
        # Caso seja TRUE, então essa condição sera executada
        if rede_social.username != rede_social.email:
            messages.error(request, 'Sua conta está vinculada a sua rede social. Clique no botão de mídia social para acessar.')
            return render(request, 'accounts_templates/login.html')

        else:
            auth.login(request, user)
            messages.success(request, f'Seja bem-vindo {user.first_name} {user.last_name}!')
            return redirect('dashboard')      
 
    except modelUser.DoesNotExist:
        messages.error(request, 'Usuário ou senha inválidos.')
        return render(request, 'accounts_templates/login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')

def register(request):
    if request.method != 'POST':
        return render(request, 'accounts_templates/register.html')
    
    nome = request.POST.get('nome')
    sobrenome = request.POST.get('Snome')
    email = request.POST.get('email')
    senha = request.POST.get('password')
    rsenha = request.POST.get('Rsenha')
    
    # Variaveis para vericar se a senha possui pelo menos:
    # uma letra maiuscula 
    # uma letra minuscula 
    # um numero.
    lower = any(chr.islower() for chr in senha)
    capital = any(chr.isupper() for chr in senha)
    numeric = any(chr.isnumeric() for chr in senha)

    if not nome or not sobrenome or not email or not senha or not rsenha:
        messages.error(request, 'Nenhum campo pode ficar vázio')
        return render(request, 'accounts_templates/register.html')
    
    try:
        validate_email(email)
    except:
        messages.error(request, 'Email inválido')
        return render(request, 'accounts_templates/register.html')

    if not capital:
        messages.error(request, 'A senha dever conter pelo menos uma letra maiúscula.')
        return render(request, 'accounts_templates/register.html')

    if not lower:
        messages.error(request, 'A senha dever conter pelo menos uma letra minúscula.')
        return render(request, 'accounts_templates/register.html')

    if not numeric:
        messages.error(request, 'A senha dever conter pelo menos um número.')
        return render(request, 'accounts_templates/register.html')

    if len(senha) < 8:
        messages.error(request, 'Senha muito curta! Senha precisa ter no minimo 8 caracteres.')
        return render(request, 'accounts_templates/register.html')

    if senha != rsenha:
        messages.error(request, 'Senhas não são iguais. Tente novamente!')
        return render(request, 'accounts_templates/register.html')
        
    if CostumerUser.objects.filter(email=email).exists():
        messages.error(request, 'Email já existe!')
        return render(request, 'accounts_templates/register.html')

    messages.success(request, 'Usuário registrado com sucesso. Agora faça login!')
    user = CostumerUser.objects.create_user(username=email, email=email, password=senha, first_name=nome, last_name=sobrenome)

    user.save()

    return redirect('login')

@login_required(redirect_field_name='#usu@rio$',login_url='login')
def dashboard(request):
    return render(request, 'accounts_templates/dashboard.html')

def locked(request):
    return render(request, 'accounts_templates/locked.html')

def Reset_Password_Complete(request):
    messages.success(request, 'Sua senha foi redefinida com SUCESSO!')
    return redirect('login')

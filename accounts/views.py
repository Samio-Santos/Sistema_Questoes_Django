from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.core.validators import validate_email
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from accounts.form import Userform
from .models import CostumerUser
from respostas.models import Resposta
from perguntas.models import Pergunta


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
            messages.success(request, f'Seja bem-vindo(a) {user.first_name} {user.last_name}!')
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
    sexo = request.POST.get('sexo')
    senha = request.POST.get('password')
    rsenha = request.POST.get('Rsenha')
    print(sexo)
    
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

    if not sexo:
        messages.error(request, 'O Campo "Sexo" não pode ficar vázio.')
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
    user = CostumerUser.objects.create_user(username=email, email=email, sexo=sexo, password=senha, first_name=nome, last_name=sobrenome)

    user.save()

    return redirect('login')

@login_required(redirect_field_name='#usu@rio$',login_url='login')
def dashboard(request):
    data = {}
    # listas para armazena as respostas certas e erradas de CADA materia 
    # para exibir no gráfico estatistico de barra
    portugues_certas = []
    portugues_erradas = []
    informatica_certas = []
    informatica_erradas = []
    logica_certas = []
    logica_erradas = []
    estatistica_certas = []
    estatistica_erradas = []
    direito_certas = []
    direito_erradas = []
    contabilidade_certas = []
    contabilidade_erradas = []
    criminologia_certas = []
    criminologia_erradas = []

    # listas para armazena o total de respostas certas e erradas
    # para exibir no gráfico estatistico de roscar
    respostas_certas = []
    respostas_erradas = []
    
    # Mosta qual o usuario está logado no sistema
    user = request.user

    # Conta o total de questões resolvidas pelo usuario
    total_respostas = Resposta.objects.filter(
        usuario=user
    ).count()

    for pergunta in Pergunta.objects.all():
        for respondida in Resposta.objects.filter(usuario=user):
            if pergunta == respondida.resposta_pergunta:
                if pergunta.alternativas_correta == respondida.resposta_usuario:
                    respostas_certas.append(respondida)

                    if respondida.materia == 'Português':
                        portugues_certas.append(respondida)

                    if respondida.materia == 'Informática':
                        informatica_certas.append(respondida)

                    if respondida.materia == 'Lógica':
                        logica_certas.append(respondida)

                    if respondida.materia == 'Estatística':
                        estatistica_certas.append(respondida)

                    if respondida.materia == 'Direito':
                        direito_certas.append(respondida)
                    
                    if respondida.materia == 'Contabilidade':
                        contabilidade_certas.append(respondida)
                    
                    if respondida.materia == 'Criminologia':
                        criminologia_certas.append(respondida)
                    
                else:
                    respostas_erradas.append(respondida)

                    if respondida.materia == 'Português':
                        portugues_erradas.append(respondida)

                    if respondida.materia == 'Informática':
                        informatica_erradas.append(respondida)

                    if respondida.materia == 'Lógica':
                        logica_erradas.append(respondida)

                    if respondida.materia == 'Estatística':
                        estatistica_erradas.append(respondida)

                    if respondida.materia == 'Direito':
                        direito_erradas.append(respondida)
                    
                    if respondida.materia == 'Contabilidade':
                        contabilidade_erradas.append(respondida)
                    
                    if respondida.materia == 'Criminologia':
                        criminologia_erradas.append(respondida)

    data['total_respostas'] = total_respostas
    data['respostas_certas'] = len(respostas_certas)
    data['respostas_erradas'] = len(respostas_erradas)

    data['portugues_certas'] = len(portugues_certas)
    data['portugues_erradas'] = len(portugues_erradas)
    data['informatica_certas'] = len(informatica_certas)
    data['informatica_erradas'] = len(informatica_erradas)
    data['logica_certas'] = len(logica_certas)
    data['logica_erradas'] = len(logica_erradas)
    data['estatistica_certas'] = len(estatistica_certas)
    data['estatistica_erradas'] = len(estatistica_erradas)
    data['direito_certas'] = len(direito_certas)
    data['direito_erradas'] = len(direito_erradas)
    data['contabilidade_certas'] = len(contabilidade_certas)
    data['contabilidade_erradas'] = len(contabilidade_erradas)
    data['criminologia_certas'] = len(criminologia_certas)
    data['criminologia_erradas'] = len(criminologia_erradas)

    return render(request, 'accounts_templates/dashboard.html', data)


def perfil_usuario(request, id):
    data = {}
    sexo = request.POST.get('sexo')
    user = CostumerUser.objects.get(id=id)
    form  = Userform(request.POST or None, request.FILES or None, instance=user)

    data['user'] = user
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.sexo = sexo
            form.save()
            messages.success(request, 'Dados atualizados com sucesso')
            return redirect('dashboard')
    
    else:
        return render(request, 'accounts_templates/perfil_user.html', data)


def locked(request):
    return render(request, 'accounts_templates/locked.html')

def Reset_Password_Complete(request):
    messages.success(request, 'Sua senha foi redefinida com SUCESSO!')
    return redirect('login')

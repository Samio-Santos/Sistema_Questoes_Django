from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

from accounts.facad_accounts import *

from django.urls import reverse_lazy
from accounts.form import Userform
from .models import CostumerUser
from respostas.models import Resposta
from perguntas.models import Pergunta

from django_pdfkit import PDFView
from django.contrib.auth.mixins import LoginRequiredMixin

# from django.db import connection

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
            messages.error(request, 'Esta conta está vinculada a um rede social abaixo!')
            return render(request, 'accounts_templates/login.html', {'notUser': 'notUser'})

        if not user:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'accounts_templates/login.html', {'invalid': 'invalid'})

        else:
            auth.login(request, user)
            messages.success(request, f'Seja bem-vindo(a) {user.first_name} {user.last_name}!')
            return redirect('dashboard')
                
 
    except modelUser.DoesNotExist:
        messages.error(request, 'Usuário não está cadastrado!')
        return render(request, 'accounts_templates/login.html', {'notUser': 'notUser'})

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

    # Variaveis para vericar se a senha possui pelo menos:
    # uma letra maiuscula 
    # uma letra minuscula 
    # um numero.
    lower = any(chr.islower() for chr in senha)
    capital = any(chr.isupper() for chr in senha)
    numeric = any(chr.isnumeric() for chr in senha)

    if not get_validacao_dados_register(request=request, nome=nome, sobrenome=sobrenome, email=email, senha=senha, rsenha=rsenha, capital=capital, lower=lower, numeric=numeric, sexo=sexo):
        return render(request, 'accounts_templates/register.html')

    else:
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

    # Acessa o model RESPOSTA
    model_resposta = Resposta.objects.filter(usuario=user).select_related("resposta_pergunta")

    for pergunta in Pergunta.objects.all():
        for respondida in model_resposta:
            if pergunta == respondida.resposta_pergunta:
                if pergunta.alternativas_correta == respondida.resposta_usuario:
                    respostas_certas.append(respondida)

                    get_resposta_certas_dashboard(respondida, portugues_certas, informatica_certas, logica_certas,  estatistica_certas, direito_certas, contabilidade_certas, criminologia_certas, data)
                else:
                    get_resposta_erradas_dashboard(respondida, portugues_erradas, informatica_erradas, logica_erradas, estatistica_erradas, direito_erradas, contabilidade_erradas, criminologia_erradas, data)
                    
                    respostas_erradas.append(respondida)

    data['total_respostas'] = total_respostas
    data['respostas_certas'] = len(respostas_certas)
    data['respostas_erradas'] = len(respostas_erradas)

    return render(request, 'accounts_templates/dashboard.html', data)


@login_required(redirect_field_name='#usu@rio$',login_url='login')
def perfil_usuario(request, id):
    if request.user.id != id:
        return redirect(reverse_lazy('perfil_user', args=[request.user.id]))
        
    data = {}
    sexo = request.POST.get('sexo')
    user = CostumerUser.objects.get(id=id)
    form  = Userform(request.POST or None, request.FILES or None, instance=user)


    if request.method == 'POST':
        if form.is_valid():
            form.sexo = sexo
            form.save()
            messages.success(request, 'Dados atualizados com sucesso')
            return redirect('dashboard')

    data['user'] = user
    data['form'] = form
    return render(request, 'accounts_templates/perfil_user.html', data)


def locked(request):
    return render(request, 'accounts_templates/locked.html')

def Reset_Password_Complete(request):
    messages.success(request, 'Sua senha foi redefinida com SUCESSO!')
    return redirect('login')

class pdfview(LoginRequiredMixin, PDFView):
    login_url = 'login'
    template_name = 'accounts_templates/relatorio.html'
    
    def get_filename(self):
        user = self.request.user.first_name
        qs = super().get_filename()
        qs = f'relatorio_{user}'
        return qs

    def render_html(self, *args, **kwargs):
        user = self.request.user
        kwargs['user'] = user
        kwargs['resposta'] = Resposta.objects.filter(usuario=user).select_related("resposta_pergunta")

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

        for pergunta in Pergunta.objects.all():
            for respondida in kwargs['resposta']:
                if pergunta == respondida.resposta_pergunta:
                    if pergunta.alternativas_correta == respondida.resposta_usuario:

                        get_resposta_certas_dashboard(respondida, portugues_certas, informatica_certas, logica_certas,  estatistica_certas, direito_certas, contabilidade_certas, criminologia_certas, kwargs)
                    else:
                        get_resposta_erradas_dashboard(respondida, portugues_erradas, informatica_erradas, logica_erradas, estatistica_erradas, direito_erradas, contabilidade_erradas, criminologia_erradas, kwargs)

        context = super().render_html(*args, **kwargs)

        return context




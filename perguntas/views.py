from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from respostas.models import Resposta
from .models import Pergunta
from random import shuffle
from perguntas.facad import *
# from django.db import connection


@login_required(redirect_field_name='#usu@rio$',login_url='login')
# Função para exibir todas as perguntas, respondidas e não respondidas
def perguntas(request, materia):
    data = {}
    user = request.user
    lista_perguntas = []

    # Faz uma iteração com models "PERGUNTA" e colocar dentro de uma lista
    for pergunta in Pergunta.objects.order_by('-id').filter(
        materia__materia__iexact=materia,
        disponivel=True
    ):
        lista_perguntas.append(pergunta)
        

    respostas = Resposta.objects.filter(
        usuario=user
    )

    # embaralha as questoes
    # Conta o total de questões da materia
    shuffle(lista_perguntas)
    count = len(lista_perguntas)

    # Pegar a resposta do usuário
    resposta_usuario = request.POST.get('resp')
    banca = request.POST.get('banca')
    disciplina = request.POST.get('materia')
    id_pergunta = request.POST.get('questao')
    
    valid_pergunta(request, user, resposta_usuario, banca, disciplina, id_pergunta)

    # Paginação
    paginator = Paginator(lista_perguntas, 4)
    page = request.GET.get('p')
    lista_perguntas = paginator.get_page(page)

    data['perguntas'] = lista_perguntas
    data['count'] = count
    data['resposta'] = respostas
    data['materia'] = materia
    return render(request, 'perguntas_templates/index.html', data)



@login_required(redirect_field_name='#usu@rio$',login_url='login')
# Função para exibir SOMENTE as perguntas NÃO resolvidas
def questoes_nao_resolvidas(request, materia):
    data = {}
    user = request.user
    lista_perguntas = []
    
    resposta = Resposta.objects.filter(
        usuario=user
    )

    # Faz uma iteração com models "PERGUNTA"
    # E retorna uma lista com perguntas não resolvidas 
    pergunta_respondida(lista_perguntas, materia, user)

    # embaralha as questoes
    # Conta o total de questões não resolvidas da materia
    shuffle(lista_perguntas)
    count = len(lista_perguntas)
    
    # Pegar a resposta do usuário, banca e a materia
    resposta_usuario = request.POST.get('resp')
    banca = request.POST.get('banca')
    disciplina = request.POST.get('materia')
    id_pergunta = request.POST.get('questao')

    valid_pergunta(request, user, resposta_usuario, banca, disciplina, id_pergunta)

    
    # Paginação
    paginator = Paginator(lista_perguntas, 4)
    page = request.GET.get('p')
    lista_perguntas = paginator.get_page(page)

    data['perguntas'] = lista_perguntas
    data['resposta'] = resposta
    data['count'] = count
    data['materia'] = materia
    data['variavel'] = 'não resolvidas'
    return render(request, 'perguntas_templates/index.html', data)

@login_required(redirect_field_name='#usu@rio$',login_url='login')
# Função para exibir SOMENTE as perguntas da banca VUNESP, CESPE 
# ou qualquer outra banca cadastrada no banco de dados
def filtro_banca(request, banca, materia):
    data = {}
    user = request.user
        
    # faz o filtro pela banca e retorna perguntas somente da banca
    #paginação e a contagem das perguntas
    filtro_banca_perguntas(request, banca, materia, data)

    # filtra somente a resposta do usuario logado
    resposta = Resposta.objects.filter(
        usuario=user
    )

    # Pegar a resposta do usuário e a materia
    resposta_usuario = request.POST.get('resp')
    disciplina = request.POST.get('materia')
    id_pergunta = request.POST.get('questao')

    valid_pergunta(request, user, resposta_usuario, banca, disciplina, id_pergunta)
    
    data['resposta'] = resposta
    data['materia'] = materia
    data['variavel'] = banca
    return render(request, 'perguntas_templates/index.html', data)

# Zera as questoes resolvidas pelo usuario
def deletar_questoes(request):
    user = request.user
    delete = request.POST.get('delete')

    if delete == "Deletar":
        Resposta.objects.filter(usuario=user).delete()
        messages.success(request, f'Suas estatísticas foram zeradas com sucesso!')
        return redirect('dashboard')
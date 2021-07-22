from django.db import models
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from respostas.models import Resposta
from .models import Pergunta


@login_required(redirect_field_name='#usu@rio$',login_url='login')
# Função para exibir todas as perguntas, respondidas e não respondidas
def perguntas(request, materia):
    data = {}
    user = request.user

    pergunta = Pergunta.objects.order_by('-id').filter(
        materia__materia__iexact=materia,
        disponivel=True
    )
    

    respostas = Resposta.objects.filter(
        usuario=user
    )

    # Conta o total de questões que a matéria possui
    count = pergunta.count()

    # Pegar a resposta do usuário
    resposta_usuario = request.POST.get('resp')
    banca = request.POST.get('banca')
    disciplina = request.POST.get('materia')
    if request.method == 'POST':
        print(resposta_usuario)
        # Identificador da pergunta vinda do template
        id_pergunta = request.POST.get('questao')
        # Gabarito da pergunta cadastrada no banco de dados
        questao = Pergunta.objects.get(id=id_pergunta)
        pergunta_respondida = request.POST.get('id_resposta')
        model_resposta = Resposta()

        if pergunta_respondida is None:
            if resposta_usuario == questao.alternativas_correta:
                model_resposta.resposta_pergunta = questao
                model_resposta.usuario = user
                model_resposta.resposta_usuario = resposta_usuario
                model_resposta.materia = disciplina
                model_resposta.banca = banca
                model_resposta.respondida = True
                
                model_resposta.save()

            else:
                model_resposta.resposta_pergunta = questao
                model_resposta.usuario = user
                model_resposta.resposta_usuario = resposta_usuario
                model_resposta.materia = disciplina
                model_resposta.banca = banca
                model_resposta.respondida = True

                model_resposta.save()
    # Paginação
    paginator = Paginator(pergunta, 4)
    page = request.GET.get('p')
    pergunta = paginator.get_page(page)

    data['perguntas'] = pergunta
    data['count'] = count
    data['resposta'] = respostas
    data['materia'] = materia
    return render(request, 'perguntas_templates/index.html', data)

@login_required(redirect_field_name='#usu@rio$',login_url='login')
# Função para exibir SOMENTE as perguntas resolvidas
def questoes_resolvidas(request, materia):
    data = {}
    user = request.user

    pergunta = Pergunta.objects.filter(
        disponivel=True
    )

    resolvidas = Resposta.objects.order_by('-id').filter(
        usuario=user,
        resposta_pergunta__materia__materia=materia,
        respondida=True
        
    )

    # Conta o total de questões resolvidas da materia
    count = resolvidas.count()
    
    # Paginação
    paginator = Paginator(resolvidas, 4)
    page = request.GET.get('p')
    resolvidas = paginator.get_page(page)

    data['resolvidas'] = resolvidas
    data['perguntas'] = pergunta
    data['count'] = count
    data['materia'] = materia
    return render(request, 'perguntas_templates/questoes_resolvidas.html', data)

@login_required(redirect_field_name='#usu@rio$',login_url='login')
# Função para exibir SOMENTE as perguntas NÃO resolvidas
def questoes_nao_resolvidas(request, materia):
    data = {}
    user = request.user
    lista = []
    
    resposta = Resposta.objects.filter(
        usuario=user
    )

    # Faz uma iteração com models "PERGUNTA"
    # E depois verifica no models "RESPOSTA" se usuário já respondeu aquela questão
    for pergunta in Pergunta.objects.order_by('-id').filter(
        materia__materia__iexact=materia,
        disponivel=True
        ):

        questoes_resolvidas = Resposta.objects.filter(
        usuario=user,
        resposta_pergunta=pergunta
        ).exists()

        # Verifica se a questão foi resolvida pelo usuário
        # Se não resolvidas, então a questão é adicionada na lista e exibida no template
        if not questoes_resolvidas:
            lista.append(pergunta)
    
    # Pegar a resposta do usuário
    resposta_usuario = request.POST.get('resp')
    banca = request.POST.get('banca')

    # Conta o total de questões não resolvidas da materia
    count = len(lista)

    if request.method == 'POST':
        # Identificador da pergunta vinda do template
        id_pergunta = request.POST.get('questao')
        # Gabarito da pergunta cadastrada no banco de dados
        questao = Pergunta.objects.get(id=id_pergunta)
        pergunta_respondida = request.POST.get('id_resposta')
        model_resposta = Resposta()

        if pergunta_respondida is None:
            if resposta_usuario == questao.alternativas_correta:
                model_resposta.resposta_pergunta = questao
                model_resposta.usuario = user
                model_resposta.resposta_usuario = resposta_usuario
                model_resposta.banca = banca
                model_resposta.respondida = True
                
                model_resposta.save()

            else:
                model_resposta.resposta_pergunta = questao
                model_resposta.usuario = user
                model_resposta.resposta_usuario = resposta_usuario
                model_resposta.banca = banca
                model_resposta.respondida = True

                model_resposta.save()
    
    # Paginação
    paginator = Paginator(lista, 4)
    page = request.GET.get('p')
    lista = paginator.get_page(page)

    data['perguntas'] = lista
    data['resposta'] = resposta
    data['count'] = count
    data['materia'] = materia
    return render(request, 'perguntas_templates/questoes_nao_resolvidas.html', data)

# Zera as questoes resolvidas pelo usuario
def deletar_questoes(request):
    user = request.user
    delete = request.POST.get('delete')

    if delete == "Deletar":
        Resposta.objects.filter(usuario=user).delete()
        messages.success(request, f'Suas estatísticas foram zeradas com sucesso!')
        return redirect('dashboard')
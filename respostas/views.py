from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from respostas.models import Resposta
from .models import Pergunta

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
# Função para exibir SOMENTE as perguntas que o usuário acertou ou errou
def questoes_certas_ou_erradas(request, var, materia):
    data = {}
    user = request.user
    respostas_certas = []
    
    model_pergunta = Pergunta.objects.filter(
        disponivel=True
    )
    
    model_resposta = Resposta.objects.order_by('-id').filter(
        usuario=user,
        resposta_pergunta__materia__materia=materia,
        respondida=True
    )

    # Logica para exibir somente as as questões que o usuário acertou ou errou
    if var == 'certas':
        for pergunta in model_pergunta:
            for resolvidas_certas in model_resposta:
                if pergunta == resolvidas_certas.resposta_pergunta:
                    if resolvidas_certas.resposta_usuario == pergunta.alternativas_correta:
                        respostas_certas.append(resolvidas_certas)
                        
    elif var == 'erradas':
        for pergunta in model_pergunta:
            for resolvidas_certas in model_resposta:
                if pergunta == resolvidas_certas.resposta_pergunta:
                    if resolvidas_certas.resposta_usuario != pergunta.alternativas_correta:
                        respostas_certas.append(resolvidas_certas)

    # Conta o total de questões resolvidas da materia
    count = len(respostas_certas)
    
    # Paginação
    paginator = Paginator(respostas_certas, 4)
    page = request.GET.get('p')
    respostas_certas = paginator.get_page(page)

    data['resolvidas'] = respostas_certas
    data['perguntas'] = model_pergunta
    data['count'] = count
    data['materia'] = materia
    return render(request, 'perguntas_templates/questoes_resolvidas.html', data)

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator

from respostas.models import Resposta
from .models import Pergunta
from accounts.models import CostumerUser

@login_required(redirect_field_name='#usu@rio$',login_url='login')
def perguntas(request):
    data = {}
    user = request.user

    pergunta = Pergunta.objects.order_by('-id').filter(
        disponivel=True
    )

    respostas = Resposta.objects.filter(
        usuario=user
    )

    # Pegar a resposta do usuário
    resposta_usuario = request.POST.get('resp')
    if request.method == 'POST':
        # Identificador da pergunta vinda do template
        id_pergunta = request.POST.get('questao')
        # Gabarito da pergunta cadastrada no banco de dados
        questao = Pergunta.objects.get(id=id_pergunta)
        model_resposta = Resposta()
        pergunta_respondida = request.POST.get('id_resposta')
        
        if pergunta_respondida is None:
            if resposta_usuario == questao.alternativas_correta:
                model_resposta.resposta_pergunta = questao
                model_resposta.usuario = user
                model_resposta.resposta_certa = resposta_usuario
                model_resposta.respondida = True
                model_resposta.save()

            else:
                model_resposta.resposta_pergunta = questao
                model_resposta.usuario = user
                model_resposta.resposta_errada = resposta_usuario
                model_resposta.respondida = True
                model_resposta.save()
    # Paginação
    paginator = Paginator(pergunta, 4)
    page = request.GET.get('p')
    pergunta = paginator.get_page(page)

    data['perguntas'] = pergunta
    data['resposta'] = respostas
    return render(request, 'perguntas_templates/index.html', data)
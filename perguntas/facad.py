from perguntas.models import Pergunta
from respostas.models import Resposta
from django.core.paginator import Paginator

def valid_pergunta(request, user, resposta_usuario, banca, disciplina, id_pergunta):
    if request.method == 'POST':
        pergunta = Pergunta.objects.get(id=id_pergunta)
        pergunta_respondida = request.POST.get('id_resposta')

        if pergunta_respondida is None:
            if resposta_usuario == pergunta.alternativas_correta:
                Resposta.send_resposta(user, pergunta, resposta_usuario, disciplina, banca)

            else:
                Resposta.send_resposta(user, pergunta, resposta_usuario, disciplina, banca)
    
        return

def pergunta_respondida(lista_perguntas, materia, user):
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
            lista_perguntas.append(pergunta)

    return lista_perguntas

def filtro_banca_perguntas(request, banca, materia, data):
    # Inicializa a variável pergunta com uma query vazia
    pergunta = Pergunta.objects.none()
    
    # Faz o filtro pela banca
    pergunta = Pergunta.objects.filter(
        disponivel=True,
        banca__banca__iexact=banca,
        materia__materia__iexact=materia,
    )
    
    # Conta o total de questões resolvidas da materia
    count = pergunta.count()

    # Paginação
    paginator = Paginator(pergunta, 4)
    page = request.GET.get('p')
    pergunta = paginator.get_page(page)

    data['count'] = count
    data['perguntas'] = pergunta

    return data
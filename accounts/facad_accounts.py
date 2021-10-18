from django.core.validators import validate_email
from django.contrib import messages
from .models import CostumerUser

def get_validacao_dados_register(**kwargs):
    request = kwargs.get('request')
    nome = kwargs.get('nome')
    sobrenome = kwargs.get('sobrenome')
    email = kwargs.get('email')
    senha = kwargs.get('senha')
    capital = kwargs.get('capital')
    rsenha = kwargs.get('rsenha')
    lower = kwargs.get('lower')
    numeric = kwargs.get('numeric')
    sexo = kwargs.get('sexo')


    if not nome or not sobrenome or not email or not senha or not rsenha:
        return messages.error(request, 'Nenhum campo pode ficar vázio')

    try:
        validate_email(email)
    except:
        return messages.error(request, 'Email inválido')

    if not capital:
        return messages.error(request, 'A senha dever conter pelo menos uma letra maiúscula.')

    if not lower:
        return messages.error(request, 'A senha dever conter pelo menos uma letra minúscula.')

    if not numeric:
        return messages.error(request, 'A senha dever conter pelo menos um número.')

    if not sexo:
        return messages.error(request, 'O Campo "Sexo" não pode ficar vázio.')

    if len(senha) < 8:
        return messages.error(request, 'Senha muito curta! Senha precisa ter no minimo 8 caracteres.')

    if senha != rsenha:
        return messages.error(request, 'Senhas não são iguais. Tente novamente!')
        
    if CostumerUser.objects.filter(email=email).exists():
        return messages.error(request, 'Email já existe!')
    
    return nome, sobrenome, email, senha, rsenha, capital,lower, numeric, sexo



def get_resposta_certas_dashboard(respondida, portugues_certas, informatica_certas, logica_certas,  estatistica_certas, direito_certas, contabilidade_certas, criminologia_certas, data):

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
    
    data['portugues_certas'] = len(portugues_certas)
    data['informatica_certas'] = len(informatica_certas)
    data['logica_certas'] = len(logica_certas)
    data['estatistica_certas'] = len(estatistica_certas)
    data['direito_certas'] = len(direito_certas)
    data['contabilidade_certas'] = len(contabilidade_certas)
    data['criminologia_certas'] = len(criminologia_certas)

    
    return data

    
def get_resposta_erradas_dashboard(respondida, portugues_erradas, informatica_erradas, logica_erradas,  estatistica_erradas, direito_erradas, contabilidade_erradas, criminologia_erradas, data):

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

    data['portugues_erradas'] = len(portugues_erradas)
    data['informatica_erradas'] = len(informatica_erradas)
    data['logica_erradas'] = len(logica_erradas)
    data['estatistica_erradas'] = len(estatistica_erradas)
    data['direito_erradas'] = len(direito_erradas)
    data['contabilidade_erradas'] = len(contabilidade_erradas)
    data['criminologia_erradas'] = len(criminologia_erradas)

    return data

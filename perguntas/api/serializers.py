# Importa os modelos necessários para a aplicação
from perguntas.models import Pergunta
from categorias.models import Materia, Banca
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from django.utils.html import strip_tags

# Importa funções para manipulação de data
from datetime import date, datetime

# Obtém a data atual no formato YYYY-MM-DD
date = date.today()
date_atual = f'{date.strftime("%Y")}-{date.strftime("%m")}-{date.strftime("%d")}'

class PerguntasSerializer(serializers.ModelSerializer):
    # Define o campo 'alternativas_correta' como uma string
    alternativas_correta = serializers.CharField()  
    # lista_field contém as alternativas válidas
    lista_field = ['A', 'B', 'C', 'D', 'E', 'Certo', 'Errado']

    class Meta:
        # Define o modelo que o serializer representa
        model = Pergunta
        # Define os campos que devem ser incluídos na representação
        fields = ['id', 'texto', 'enunciado', 'alternativas_Multiplasescolhas', 'alternativas_correta', 'disponivel', 'materia', 'banca']

    def to_representation(self, instance):
        # Obtém a representação padrão do modelo
        representation = super().to_representation(instance)
        
        # Remove tags HTML do campo 'texto' e 'enunciado' usando strip_tags
        representation['enunciado'] = strip_tags(representation['enunciado']).replace('\r', ' ').replace('\n', ' ').replace('&nbsp;', '')
        representation['texto'] = strip_tags(representation['texto']).replace('\r', ' ').replace('\n', ' ')

        # Verifica se a banca é 'cespe' (case-insensitive)
        if instance.banca and instance.banca.banca.lower() == 'cespe':
            # Remove o campo 'alternativas_Multiplasescolhas' se a banca for 'cespe'
            representation.pop('alternativas_Multiplasescolhas', None)

        return representation

    def validate(self, attrs):
        # Obtém os valores dos atributos passados
        alternativas_Multiplasescolhas = attrs.get('alternativas_Multiplasescolhas')
        alternativas_correta = attrs.get('alternativas_correta')
        banca = attrs.get('banca')

        # Valida se a banca é 'Vunesp' e se o campo 'alternativas_Multiplasescolhas' está vazio
        if str(banca) == 'Vunesp' and alternativas_Multiplasescolhas is None:
            raise serializers.ValidationError({'alternativas_Multiplasescolhas': 'O campo "alternativas_Multiplasescolhas" não pode ficar em branco'})

        # Valida se a banca é 'Cespe' e se a alternativa correta é uma das opções inválidas
        if str(banca) == 'Cespe' and alternativas_correta.capitalize() in ['A', 'B', 'C', 'D', 'E']:
            raise serializers.ValidationError({'alternativas_correta': 'Escolha inválida. As opções válidas são: "Certo" ou "Errado"'})
 
        # Valida se 'alternativas_Multiplasescolhas' está preenchido e se a alternativa correta é 'Certo' ou 'Errado'
        if alternativas_Multiplasescolhas and alternativas_correta.capitalize() in ["Certo", "Errado"]:
            raise serializers.ValidationError({'alternativas_correta': 'Escolha inválida. As opções válidas são: A, B, C, D, E.'})
        
        return attrs
    
    def validate_enunciado(self, enunciado):
        # Verifica se o campo 'enunciado' não está vazio
        if enunciado == '':
            raise serializers.ValidationError('O campo "enunciado" não pode estar vazio.')
        return enunciado

    def validate_alternativas_correta(self, alternativas_correta):
        # Verifica se a alternativa correta está nas opções válidas
        if alternativas_correta.capitalize() not in self.lista_field:
            raise serializers.ValidationError('Escolha inválida. As opções válidas são: A, B, C, D, E, Certo, Errado.')
        
        # Verifica se o campo 'alternativas_correta' não está vazio
        if alternativas_correta == '':
            raise serializers.ValidationError('O campo "alternativas_correta" não pode estar vazio.')
        return alternativas_correta.capitalize()

    def validate_materia(self, materia):
        # Verifica se o campo 'materia' não está vazio
        if materia == '':
            raise serializers.ValidationError('O campo "materia" não pode estar vazio.')
        return materia

    def validate_banca(self, banca):
        # Verifica se o campo 'banca' não está vazio
        if banca == '':
            raise serializers.ValidationError('O campo "banca" não pode estar vazio.')
        return banca

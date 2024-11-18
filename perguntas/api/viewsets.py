from perguntas.api.serializers import PerguntasSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import serializers, status
from categorias.models import Materia, Banca

from datetime import datetime, date

from perguntas.models import Pergunta

date = date.today()
date_atual = f'{date.strftime("%Y")}-{date.strftime("%m")}-{date.strftime("%d")}'

class PerguntaAllViewSet(ModelViewSet):
    queryset = Pergunta.objects.all().order_by('-id')
    serializer_class = PerguntasSerializer
    # permission_classes = [IsAuthenticated]

class PerguntaInformaticaViewSet(ModelViewSet):
    queryset = Pergunta.objects.filter(materia__materia='Informática').order_by('-id')
    serializer_class = PerguntasSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    
class PerguntaLogicaViewSet(ModelViewSet):
    queryset = Pergunta.objects.filter(materia__materia='Lógica')
    serializer_class = PerguntasSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class PerguntaDireitoViewSet(ModelViewSet):
    queryset = Pergunta.objects.filter(materia__materia='Direito')
    serializer_class = PerguntasSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

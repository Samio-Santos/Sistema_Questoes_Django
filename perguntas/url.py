from django.urls import path
from .views import perguntas, questoes_resolvidas, questoes_nao_resolvidas

urlpatterns = [
    path('matéria/<str:materia>', perguntas, name='categoria_materia'),
    path('questoes-resolvidas/<str:materia>', questoes_resolvidas, name='resolvidas'),
    path('questoes-nao-resolvidas/<str:materia>', questoes_nao_resolvidas, name='nao_resolvidas'),
]
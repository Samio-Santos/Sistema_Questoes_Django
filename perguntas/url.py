from django.urls import path
from .views import filtro_banca, perguntas, questoes_resolvidas, questoes_nao_resolvidas, deletar_questoes

urlpatterns = [
    path('matéria/<str:materia>', perguntas, name='categoria_materia'),
    path('questoes-resolvidas/<str:materia>', questoes_resolvidas, name='resolvidas'),
    path('questoes-nao-resolvidas/<str:materia>', questoes_nao_resolvidas, name='nao_resolvidas'),
    path('<str:banca>/<str:materia>', filtro_banca, name='filtro_banca'),
    path('deletar_questoes_resolvidas', deletar_questoes, name='deletar_questoes_resolvidas'),
]
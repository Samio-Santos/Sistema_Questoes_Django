from django.urls import path
from respostas.views import questoes_certas_ou_erradas, questoes_resolvidas

urlpatterns = [
    path('questoes-resolvidas/<str:materia>', questoes_resolvidas, name='resolvidas'),
    path('questões_<str:var>/<str:materia>', questoes_certas_ou_erradas, name='certas'),
]
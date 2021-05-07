from django.urls import path
from .views import perguntas

urlpatterns = [
    path('index/', perguntas, name='index'),
]
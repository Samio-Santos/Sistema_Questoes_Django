from django.db import models
from perguntas.models import Pergunta
from accounts.models import CostumerUser
from django.utils import timezone

class Resposta(models.Model):
    usuario = models.ForeignKey(CostumerUser, on_delete=models.CASCADE)
    resposta_pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE, blank=True, null=True)
    resposta_usuario = models.CharField(max_length=10, blank=True, null=True, default=None)
    materia = models.CharField(max_length=20, blank=True, null=True, default=None)
    banca = models.CharField(max_length=20, blank=True, null=True, default=None)
    respondida = models.BooleanField(default=False)
    data = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.usuario.username

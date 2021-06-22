from django.db import models
from categorias.models import Materia, Banca

class Pergunta(models.Model):
    texto = models.TextField(blank=True, null=True)
    enunciado = models.TextField()
    alternativas_Multiplasescolhas = models.JSONField(
    default={
        "A": " ", 
        "B": " ", 
        "C": " ",
        "D": " ", 
        "E": " ",
    }, blank=True, null=True)
    alternativas_correta = models.CharField(max_length=10, 
    choices=[
        ('A', 'A'),
        ('B', 'B'),
        ('C', 'C'),
        ('D', 'D'),
        ('E', 'E'),
        ('Certo', 'Certo'),
        ('Errado', 'Errado')
    ])
    materia = models.ForeignKey(Materia ,on_delete=models.CASCADE)
    banca = models.ForeignKey(Banca, on_delete=models.CASCADE)
    disponivel = models.BooleanField(default=False)

    def __str__(self):
        return self.enunciado

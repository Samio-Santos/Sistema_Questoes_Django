from django.db import models
from django.contrib.auth.models import AbstractUser


class CostumerUser(AbstractUser):
    sexo = models.CharField(max_length=15, blank=True, null=True, default=None)
    biografia = models.TextField(blank=True)
    imagem = models.ImageField(blank=True, upload_to='fotoPerfil')
from django.db import models

class Banca(models.Model):
    banca = models.CharField(max_length=50, verbose_name='Nome banca')

    def __str__(self):
        return self.banca

class Materia(models.Model):
    materia = models.CharField(max_length=50, verbose_name='Nome materia')

    def __str__(self):
        return self.materia

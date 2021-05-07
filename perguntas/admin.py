from django.contrib import admin
from .models import Pergunta

class PerguntaAdmin(admin.ModelAdmin):
    list_display = ('id', 'enunciado','materia', 'banca', 
    'disponivel')
    list_editable = ('disponivel',)
    list_display_links = ('id', 'enunciado',)
    # readonly_fields = ['enunciado']

admin.site.register(Pergunta, PerguntaAdmin)

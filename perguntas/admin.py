from django.contrib import admin
from .models import Pergunta
from django_summernote.admin import SummernoteModelAdmin


class PerguntaAdmin(SummernoteModelAdmin):
    list_display = ('id', 'enunciado','materia', 'banca', 
    'disponivel')
    list_editable = ('disponivel',)
    list_display_links = ('id', 'enunciado',)
    summernote_fields = 'texto', 'enunciado', 'alternativas_Multiplasescolhas'

admin.site.register(Pergunta, PerguntaAdmin)

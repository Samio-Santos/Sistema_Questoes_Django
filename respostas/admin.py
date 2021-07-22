from django.contrib import admin
from .models import Resposta

class RespostaAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'resposta_usuario', 'materia', 'banca', 
    'data')
    list_display_links = ('id', 'usuario',)
    # summernote_fields = 'enunciado', 'alternativas_Multiplasescolhas'


admin.site.register(Resposta, RespostaAdmin)

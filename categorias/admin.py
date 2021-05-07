from django.contrib import admin
from .models import Banca, Materia

class BancaAdmin(admin.ModelAdmin):
    list_display = ('id', 'banca')
    list_display_links = ('id', 'banca')

class MateriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'materia')
    list_display_links = ('id', 'materia')


admin.site.register(Banca, BancaAdmin)
admin.site.register(Materia, MateriaAdmin)
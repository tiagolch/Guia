from django.contrib import admin
from .models import *


@admin.register(Ministerio)
class MinisterioAdmin(admin.ModelAdmin):
    list_display = ['nome_ministerio']


@admin.register(Funcao)
class FuncaoAdmin(admin.ModelAdmin):
    list_display = ['funcao']


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'funcao', 'email', 'celular']


@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'funcao', 'datas', 'ultima_alteracao']
    list_filter = ['funcao', 'data']
    search_fields = ['nome', 'funcao']




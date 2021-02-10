from django.contrib import admin
from .models import *


@admin.register(Ministerio)
class MinisterioAdmin(admin.ModelAdmin):
    list_display = ['nome_ministerio', 'funcao']


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'celular']


@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'get_data' ,'get_ultima_alteracao']
    list_filter = [ 'data']
    search_fields = ['nome']




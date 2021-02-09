from django.contrib import admin
from .models import *


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'celular']


@admin.register(Escala)
class EscalaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'dia', 'get_data', 'get_ultima_alteracao']






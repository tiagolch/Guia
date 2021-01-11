from django.shortcuts import render
from .models import *


def index(request):
    return render(request, 'index.html')


def lista_escala(request):
    busca = request.GET.get('buscar')
    if busca:
        resultado = Escala.objects.filter(nome__icontains=busca)
        resultado = {
            'lista': resultado
        }
    else:
        resultado = Escala.objects.order_by('data')
        resultado = {
            'lista': resultado
        }
    return render(request, 'lista_escala.html', resultado)


from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def lista_escala(request):
    return render(request, 'lista_escala.html')


from django.urls import path
from . import views


urlpatterns = [

    path('', views.index, name='index'),
    path('lista_escala', views.lista_escala, name='lista_escala'),

]
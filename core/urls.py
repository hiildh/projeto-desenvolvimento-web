from django.urls import path
from .views import listar_noticias, listar_celulares

urlpatterns = [
    path('noticias/', listar_noticias, name='listar_noticias'),
    path('celulares/', listar_celulares, name='listar_celulares'),
]

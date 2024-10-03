from django.urls import path
from .views import listar_noticias, listar_celulares, cadastro_user

urlpatterns = [
    path('noticias/', listar_noticias, name='listar_noticias'),
    path('celulares/', listar_celulares, name='listar_celulares'),
    path('cadastro_user/', cadastro_user, name='cadastro_user'),
]

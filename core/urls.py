from django.urls import path
from .views import adicionar_noticia, listar_noticias, listar_celulares, cadastro_user
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('noticias/', listar_noticias, name='listar_noticias'),
    path('adicionar-noticia/', adicionar_noticia, name='adicionar_noticia'),
    path('celulares/', listar_celulares, name='listar_celulares'),
    path('cadastro_user/', cadastro_user, name='cadastro_user'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Adiciona login
]

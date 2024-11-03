from django.urls import path
from .views import adicionar_noticia, comentar, listar_noticias, listar_celulares, cadastro_user, adicionar_celular, gerar_home, detalhar_celular
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', gerar_home, name='index'),
    path('detalhar-celular/<int:id>/', detalhar_celular, name='detalhar_celular'),
    path('comentar/<int:id>/', comentar, name='comentar'),
    path('noticias/', listar_noticias, name='listar_noticias'),
    path('adicionar-noticia/', adicionar_noticia, name='adicionar_noticia'),
    path('adicionar-celular/', adicionar_celular, name='adicionar_celular'),
    path('celulares/', listar_celulares, name='listar_celulares'),
    path('cadastro_user/', cadastro_user, name='cadastro_user'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),  # Adiciona login
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Adiciona logout
]

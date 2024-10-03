from django.shortcuts import render
from .models import Noticia, Celular

# View para listar notícias
def listar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {'noticias': noticias})

# View para listar celulares
def listar_celulares(request):
    celulares = Celular.objects.all()
    return render(request, 'celulares.html', {'celulares': celulares})

def cadastro_user(request):
    return render(request, 'cadastro_user.html')
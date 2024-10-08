from django.shortcuts import render, redirect
from .models import Noticia, Celular
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

# View para listar notícias
def listar_noticias(request):
    noticias = Noticia.objects.all()
    return render(request, 'noticias.html', {'noticias': noticias})

def adicionar_noticia(request):
    
    # Cria uma nova notícia com os dados que você inserir manualmente
    noticia = Noticia.objects.create(
        titulo="Review Galaxy S24 FE | Um celular com bateria boa e desempenho suficiente",
        conteudo="O Galaxy S24 FE é o novo celular intermediário premium da Samsung, parte da linha Fan Edition. Muito parecido com o Galaxy S24+ em visual e desempenho, o smartphone chega sem muitas novidades ou diferenciais, em posição confusa em relação aos demais modelos de 2024. Confira, no review a seguir, os prós e contras do Galaxy S24 FE e saiba para quem ele é bom.",
        autor="canaltech",  # O nome do site ou fonte da notícia
        link="https://canaltech.com.br/produto/samsung/galaxy-s24-fe/analise/",
        imagem_link="https://t.ctcdn.com.br/bUNn0l9aEu5hggZUfprOrscEZ14=/1024x576/smart/i941627.jpeg"
    )

    # Retorna uma resposta simples para confirmar que a notícia foi criada
    return HttpResponse(f"Notícia '{noticia.titulo}' adicionada com sucesso!")

def adicionar_celular(request):
    # Cria um novo celular com os dados que você inserir manualmente
    celular = Celular.objects.create(
        nome="Samsung Galaxy S24 FE",
        descricao="O Galaxy S24 FE é o novo celular intermediário premium da Samsung, parte da linha Fan Edition. Muito parecido com o Galaxy S24+ em visual e desempenho, o smartphone chega sem muitas novidades ou diferenciais, em posição confusa em relação aos demais modelos de 2024. Confira, no review a seguir, os prós e contras do Galaxy S24 FE e saiba para quem ele é bom.",
        modelo="S24 FE",
        fabricante="Samsung",
        processador="Exynos 2200",
        velocidade_processador=2.9,
        memoria_ram=8,
        armazenamento=128,
        tamanho_tela=6.7,
        resolucao_tela="FHD+",
        velocidade_clock=120,
        bateria=4500,
        modelo_bateria="Li-Po",
        camera=108,
        tipo_conexao="4G",
        link_venda="https://www.samsung.com.br/smartphones/galaxy-s24-fe/"
    )
    return HttpResponse(f"Celular '{celular.nome}' adicionado com sucesso!")


# View para listar celulares
def listar_celulares(request):
    celulares = Celular.objects.all()
    return render(request, 'celulares.html', {'celulares': celulares})

def cadastro_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        # Verifica se as senhas coincidem
        if password != confirm_password:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'cadastro_user.html')

        # Verifica se o usuário já existe
        if User.objects.filter(username=username).exists():
            messages.error(request, 'O nome de usuário já está em uso.')
            return render(request, 'cadastro_user.html')

        # Verifica se o email já está em uso
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Este email já está em uso.')
            return render(request, 'cadastro_user.html')

        # Cria o usuário
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()

        messages.success(request, 'Usuário registrado com sucesso! Faça login.')
        return redirect('login')  # Redireciona para a página de login

    return render(request, 'cadastro_user.html')
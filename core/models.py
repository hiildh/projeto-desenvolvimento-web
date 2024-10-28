from django.db import models
from django.contrib.auth.models import User

# Model para armazenar notícias sobre celulares
class Noticia(models.Model):
    titulo = models.CharField(max_length=200)
    conteudo = models.TextField()
    autor = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField(auto_now_add=True)
    link = models.URLField(max_length=200)
    imagem_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.titulo

# Model para armazenar celulares com links para compra
class Celular(models.Model):
    nome = models.CharField(max_length=100, default='')
    descricao = models.TextField(default='')
    modelo = models.CharField(max_length=100, default='')
    fabricante = models.CharField(max_length=100, default='')
    processador = models.CharField(max_length=100, default='')
    velocidade_processador = models.FloatField(default=0.0)
    memoria_ram = models.IntegerField(default=0)
    armazenamento = models.IntegerField(default=0)
    tamanho_tela = models.FloatField(default=0.0)
    resolucao_tela = models.CharField(max_length=100, default='')
    velocidade_clock = models.FloatField(default=0.0)
    bateria = models.IntegerField(default=0)
    modelo_bateria = models.CharField(max_length=100, default='')
    camera = models.FloatField(default=0.0)
    tipo_conexao = models.CharField(max_length=100, default='')
    link_venda = models.URLField(max_length=200, default='')
    imagem_link = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return f'{self.nome} - {self.modelo}'

# Model para comentários nas notícias ou celulares
class Comentario(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    celular = models.ForeignKey(Celular, null=True, blank=True, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    avaliacao = models.IntegerField(default=0)

    def __str__(self):
        return f'Comentário de {self.usuario} em {self.noticia or self.celular}'

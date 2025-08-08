from django.db import models
from django.contrib.auth.models import User

# Create your models here.
TIPOS_USUARIO = [
    ('administrador', 'Administrador'),
    ('comum', 'Comum')
]

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    tipo_usuario = models.CharField(max_length=20, choices=TIPOS_USUARIO, default='comum')

    def __str__(self):
        return f'Perfil de {self.user.username}. Seu tipo é {self.tipo_usuario}'

class Filme(models.Model):
    titulo = models.CharField(max_length=100, null=False)
    genero = models.CharField(max_length=50, choices=[("acao", "Ação"), ("aventura", "Aventura"), ("misterio", "Mistério"),  ("ficção","Ficção")], null=False)
    ano_lancamento = models.IntegerField(null=False)
    descricao = models.TextField(max_length=500, default='')
    diretor = models.CharField(max_length=100, null=False)
    imagem = models.ImageField(upload_to='imagens_filmes/', blank=True, null=True)

    def __str__(self):
        return self.titulo
    
class Entry(models.Model):
    """Caixa de texto do tópico que o usuario está aprendendo"""
    movie =  models.ForeignKey(Filme, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        """Retorna uma representação em string do model"""
        return self.text[:50]+'...'
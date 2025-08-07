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
    genero = models.CharField(max_length=50, default='Sem Gênero', null=False)
    ano_lancamento = models.IntegerField(null=False)
    descricao = models.TextField(max_length=500, default='Sem Descrição')
    diretor = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.titulo

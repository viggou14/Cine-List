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

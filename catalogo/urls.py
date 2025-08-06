from django.urls import path
#from . import views
from .views import home, filmes, filmesVistos, perfil

urlpatterns = [
    path('', home, name='home'),
    path('filmes', filmes, name='filmes'), 
    path('filmesVistos', filmesVistos, name='filmesVistos'),
    path('perfil', view=perfil, name='perfil')
]

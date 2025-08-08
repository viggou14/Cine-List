from django.urls import path
#from . import views
from .views import home, login_view, cadastro, ver_filmes, adicionar_filme, editar_filme, remover_filme, ver_filme

urlpatterns = [
    path('', home, name='home'),
    path('login', login_view, name='login_view'),
    path('cadastro', cadastro, name='cadastro'),
    path('ver_filmes', ver_filmes, name='ver_filmes'),
    path('adicionar_filme', adicionar_filme, name='adicionar_filme'),
    path('editar_filme/<int:filme_id>', editar_filme, name='editar_filme'),
    path('filme/remover/<int:filme_id>/', remover_filme, name='remover_filme'),
    path('filme/<int:filme_id>/', ver_filme, name='ver_filme'),
]

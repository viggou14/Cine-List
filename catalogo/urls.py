from django.urls import path
#from . import views
from .views import home, login_view, cadastro, ver_filmes, adicionar_filme

urlpatterns = [
    path('', home, name='home'),
    path('login', login_view, name='login_view'),
    path('cadastro', cadastro, name='cadastro'),
    path('ver_filmes', ver_filmes, name='ver_filmes'),
    path('adicionar_filme', adicionar_filme, name='adicionar_filme')
]

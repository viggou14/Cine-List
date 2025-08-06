from django.urls import path
#from . import views
from .views import home, login, cadastro

urlpatterns = [
    path('', home, name='home'),
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro'),
]

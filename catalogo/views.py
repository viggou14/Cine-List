from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'catalogo/home.html')

def filmes(request):
    return render(request, 'catalogo/filmes.html')

def filmesVistos(request):
    return HttpResponse("<h1>Filmes que você já assistiu:</h1>")

def perfil(request):
    return HttpResponse("<h1>Seu Perfil</h1>")
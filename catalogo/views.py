from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, Http404, HttpResponseForbidden
from django.contrib import messages
from .forms import CadastroForm, FilmeForm, EntryForm
from django.contrib.auth.models import User
from .models import Perfil, Filme, Entry
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.

def home(request):
    return render(request, 'catalogo/home.html')

def login_view(request):
    if request.method != 'POST':
        form = AuthenticationForm()
    else:
        form = AuthenticationForm(data = request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('home')
    context = {'form': form}
    return render(request, 'catalogo/login.html', context)
 


def cadastro(request):
    if request.method != 'POST':
        form = CadastroForm()
    else:
        form = CadastroForm(request.POST)
        if form.is_valid():
            if request.POST['password'] == request.POST['confirm_password']:
                user = User.objects.create_user(username=form.cleaned_data['username'], email=form.cleaned_data['email'], password=form.cleaned_data['password'])
                perfil = Perfil.objects.create(user=user, tipo_usuario=form.cleaned_data['tipo_usuario'])
                user.save()
                perfil.save()
                messages.success(request, 'Cadastro realizado com sucesso!')
                return redirect('login_view')
            else:
                messages.error(request, 'As senha não conferem')
        else:
            messages.error(request, 'Erro ao cadastrar o usuário')

    context = {'form': form}
    return render(request, 'catalogo/cadastro.html', context)
@login_required
def ver_filmes(request):
    filmes = Filme.objects.all()
    context = {'filmes': filmes}
    return render(request, 'catalogo/ver_filmes.html', context)
@login_required
def adicionar_filme(request):
    if request.method != 'POST':
        form = FilmeForm()
    else:
        form = FilmeForm(request.POST, request.FILES)
        if form.is_valid() and request.user.perfil.tipo_usuario =="administrador":
            form.save()
            return redirect('ver_filmes')
    
    context = {'form': form}
    return render(request, 'catalogo/adicionar_filme.html', context)
@login_required
def editar_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)

    if request.method == 'POST':
        form = FilmeForm(request.POST, instance=filme)
        if form.is_valid():
            form.save()
            return redirect('ver_filmes')
    else:
        form = FilmeForm(instance=filme)
    context = {'form': form, 'filme': filme}

    return render(request, 'catalogo/editar_filme.html', context)

def remover_filme(request, filme_id):
    filme = get_object_or_404(Filme, id=filme_id)
    filme.delete()
    return redirect('ver_filmes')

def ver_filme(request, filme_id):
    # Verifica se o usuário está autenticado e é comum
    if not request.user.is_authenticated or request.user.is_staff or request.user.is_superuser:
        return HttpResponseForbidden("Acesso negado.")

    filme = get_object_or_404(Filme, id=filme_id)
    context = {'filme': filme}
    return render(request, 'catalogo/ver_filme.html', context)
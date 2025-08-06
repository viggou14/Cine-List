from django import forms
from django.contrib.auth.models import User
from .models import Perfil, TIPOS_USUARIO

class CadastroForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Senha')
    confirm_password = forms.CharField(widget=forms.PasswordInput, label='Confirmar Senha')
    tipo_usuario = forms.ChoiceField(choices=TIPOS_USUARIO, label='Tipo de Usuário', widget=forms.Select(attrs={'class': 'form-select'}))

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'})
        }
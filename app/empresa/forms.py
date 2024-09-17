from django import forms

from app.accounts.models import User
from .models import Empresa, Organizacao, GestorRh

class EmpresaForm(forms.Form):
    razao_social = forms.CharField(max_length=150, label='Razão Social', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nome_fantasia = forms.CharField(max_length=150, label='Nome Fantasia', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cnpj = forms.CharField(max_length=14, label='CNPJ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep = forms.CharField(max_length=8, label='CEP', widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco = forms.CharField(max_length=255, label='Endereço', widget=forms.TextInput(attrs={'class': 'form-control'}))
    uf = forms.CharField(max_length=2, label='UF', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade = forms.CharField(max_length=100, label='Cidade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    bairro = forms.CharField(max_length=100, label='Bairro', widget=forms.TextInput(attrs={'class': 'form-control'}))
    numero = forms.CharField(max_length=10, label='Número', widget=forms.TextInput(attrs={'class': 'form-control'}))
    complemento = forms.CharField(max_length=100, required=False, label='Complemento', widget=forms.TextInput(attrs={'class': 'form-control'}))
    logomarca = forms.ImageField(required=False, label='Logomarca', widget=forms.FileInput(attrs={'class': 'form-control'}))
    cnae = forms.CharField(max_length=10, label='CNAE', widget=forms.TextInput(attrs={'class': 'form-control'}))
    porte = forms.Select(attrs={'class': 'form-control'})
    organizacao = forms.Select(attrs={'class': 'form-control'})

class OrganizacaoForm(forms.Form):
    nome = forms.CharField(max_length=50, label='Descrição', widget=forms.TextInput(attrs={'class': 'form-control'}))
    usuario_admin = forms.Select(attrs={'class': 'form-control'})


class GestorRhForm(forms.Form):
    empresa = forms.ModelChoiceField(queryset=Empresa.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))
    usuario = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.Select(attrs={'class': 'form-control'}))


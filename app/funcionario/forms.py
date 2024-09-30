from django import forms

from app.empresa.models import Empresa
from .models import Funcionario

class FuncionarioForm(forms.Form):
    nome = forms.CharField(max_length=150, label='Nome', widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(max_length=200, label='E-mail', widget=forms.TextInput(attrs={'class': 'form-control'}))
    empresa = forms.IntegerField()
    matricula = forms.CharField(max_length=20, label='Matrícula', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(max_length=11, label='CPF', widget=forms.TextInput(attrs={'class': 'form-control'}))
    telefone = forms.CharField(max_length=15, required=False, label='Telefone', widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_nascimento = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    genero = forms.ChoiceField(choices=[
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
        ('N', 'Prefiro não informar')
    ], label='Gênero', widget=forms.Select(attrs={'class': 'form-control'}))
    raca_cor = forms.CharField(max_length=50, label='Raça/Cor', widget=forms.TextInput(attrs={'class': 'form-control'}))
    nacionalidade = forms.CharField(max_length=50, label='Nacionalidade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    escolaridade = forms.CharField(max_length=50, label='Escolaridade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cep = forms.CharField(max_length=8, label='CEP', widget=forms.TextInput(attrs={'class': 'form-control'}))
    endereco = forms.CharField(max_length=255, label='Endereço', widget=forms.TextInput(attrs={'class': 'form-control'}))
    cidade = forms.CharField(max_length=100, label='Cidade', widget=forms.TextInput(attrs={'class': 'form-control'}))
    uf = forms.CharField(max_length=2, label='UF', widget=forms.TextInput(attrs={'class': 'form-control'}))
    data_inicio = forms.DateField(label='Data de Início', widget=forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}))
    ativo = forms.BooleanField(required=False, label='Ativo', widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    regime_contrato = forms.CharField(max_length=50, label='Regime de Contrato', widget=forms.TextInput(attrs={'class': 'form-control'}))
    motivo_termino = forms.CharField(max_length=255, required=False, label='Motivo do Término', widget=forms.TextInput(attrs={'class': 'form-control'}))
    local_de_trabalho = forms.CharField(max_length=100, label='Local de Trabalho', widget=forms.TextInput(attrs={'class': 'form-control'}))
    gestor = forms.Select(attrs={'class': 'form-control'})

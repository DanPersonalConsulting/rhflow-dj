from django.db import models
from app.abstractmodel.models import TimestampableMixin
from app.accounts.models import User

class Empresa(TimestampableMixin):
    razao_social = models.CharField(max_length=150, verbose_name='Razão Social')
    nome_fantasia = models.CharField(max_length=150, verbose_name='Nome Fantasia')
    cnpj = models.CharField(max_length=14, unique=True, verbose_name='CNPJ')
    cep = models.CharField(max_length=8, verbose_name='CEP')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    uf = models.CharField(max_length=2, verbose_name='UF')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    bairro = models.CharField(max_length=100, verbose_name='Bairro')
    numero = models.CharField(max_length=10, verbose_name='Número')
    complemento = models.CharField(max_length=100, blank=True, verbose_name='Complemento')
    logomarca = models.ImageField(upload_to='logomarcas/', blank=True, null=True, verbose_name='Logomarca')
    cnae = models.CharField(max_length=10, verbose_name='CNAE')
    porte = models.ForeignKey('Porte', on_delete=models.SET_NULL, null=True, verbose_name='Porte')

    def __str__(self):
        return self.nome_fantasia


class Porte(TimestampableMixin):
    porte = models.CharField(max_length=50, unique=True, verbose_name='Porte')
    descricao = models.TextField(blank=True, verbose_name='Descrição')

    def __str__(self):
        return self.porte


class GestorRh(TimestampableMixin):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')

    def __str__(self):
        return f'{self.usuario.username} - {self.empresa.nome_fantasia}'


class TabelaSalarial(TimestampableMixin):
    versao = models.CharField(max_length=10, verbose_name='Versão')
    ativa = models.BooleanField(default=True, verbose_name='Ativa')
    data_inicio = models.DateField(verbose_name='Data de Início')
    data_fim = models.DateField(null=True, blank=True, verbose_name='Data de Fim')
    simulacao = models.BooleanField(default=False, verbose_name='Simulação')
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, verbose_name='Empresa')

    def __str__(self):
        return f'Versão {self.versao} - {self.empresa.nome_fantasia}'


class ClasseSalarial(TimestampableMixin):
    nome = models.CharField(max_length=50, verbose_name='Nome')
    inicial = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Inicial')
    medio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Médio')
    final = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Final')
    tabela_salarial = models.ForeignKey(TabelaSalarial, on_delete=models.CASCADE, verbose_name='Tabela Salarial')

    def __str__(self):
        return f'{self.nome} - {self.tabela_salarial.versao}'
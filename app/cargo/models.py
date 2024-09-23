from django.db import models
from app.abstractmodel.models import TimestampableMixin
from app.empresa.models import ClasseSalarial


class Cargo(TimestampableMixin):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código')
    missao = models.TextField(verbose_name='Missão')
    responsabilidade = models.TextField(verbose_name='Responsabilidade')
    complexidade = models.CharField(max_length=50, verbose_name='Complexidade')
    nivel = models.CharField(max_length=50, verbose_name='Nível')
    trilha = models.CharField(max_length=50, verbose_name='Trilha')
    eixo = models.CharField(max_length=50, verbose_name='Eixo')
    classe = models.ForeignKey(ClasseSalarial, on_delete=models.SET_NULL, null=True, verbose_name='Classe Salarial')
    

    def __str__(self):
        return f'{self.nome} ({self.codigo})'


class RequisitoExperiencia(TimestampableMixin):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    tempo = models.PositiveIntegerField(verbose_name='Tempo (meses)')
    obrigatorio = models.BooleanField(default=True, verbose_name='Obrigatório')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='requisitos_experiencia', verbose_name='Cargo')

    def __str__(self):
        return f'{self.nome} - {self.tempo} meses'


class RequisitoCertificado(TimestampableMixin):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    tempo = models.PositiveIntegerField(verbose_name='Tempo (meses)')
    liquido = models.BooleanField(default=False, verbose_name='Tempo Líquido')
    link = models.URLField(blank=True, verbose_name='Link')
    obrigatorio = models.BooleanField(default=True, verbose_name='Obrigatório')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='requisitos_certificados', verbose_name='Cargo')

    def __str__(self):
        return self.nome


class RequisitoConhecimento(TimestampableMixin):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    descricao = models.TextField(blank=True, verbose_name='Descrição')
    obrigatorio = models.BooleanField(default=True, verbose_name='Obrigatório')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='requisitos_conhecimento', verbose_name='Cargo')

    def __str__(self):
        return self.nome


class RequisitoEscolaridade(TimestampableMixin):
    nivel = models.CharField(max_length=100, verbose_name='Nível')
    area = models.CharField(max_length=100, verbose_name='Área')
    status = models.CharField(max_length=50, verbose_name='Status')
    obrigatorio = models.BooleanField(default=True, verbose_name='Obrigatório')
    cargo = models.ForeignKey(Cargo, on_delete=models.CASCADE, related_name='requisitos_escolaridade', verbose_name='Cargo')

    def __str__(self):
        return f'{self.nivel} em {self.area} - {self.status}'


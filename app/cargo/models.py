from django.db import models
from app.abstractmodel.models import TimestampableMixin
from app.empresa.models import ClasseSalarial


class Cargo(TimestampableMixin):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    codigo = models.CharField(max_length=20, unique=True, verbose_name='Código')
    criticidade = models.CharField(max_length=50, verbose_name='Criticidade')
    missao = models.TextField(verbose_name='Missão')
    responsabilidade = models.TextField(verbose_name='Responsabilidade')
    classe_salarial = models.ForeignKey(ClasseSalarial, on_delete=models.SET_NULL, null=True, verbose_name='Classe Salarial')
    complexidade = models.CharField(max_length=50, verbose_name='Complexidade')
    tipo = models.CharField(max_length=50, verbose_name='Tipo')
    nivel = models.CharField(max_length=50, verbose_name='Nível')
    eixo = models.CharField(max_length=50, verbose_name='Eixo')
    carga_horaria = models.PositiveIntegerField(verbose_name='Carga Horária')

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


from django.db import models
from app.abstractmodel.models import TimestampableMixin

class Funcionario(TimestampableMixin):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    matricula = models.CharField(max_length=20, unique=True, verbose_name='Matrícula')
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF')
    telefone = models.CharField(max_length=15, blank=True, verbose_name='Telefone')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    genero = models.CharField(
        max_length=20, 
        choices=[
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('O', 'Outro'),
            ('N', 'Prefiro não informar')
        ],
        verbose_name='Gênero'
    )
    raca_cor = models.CharField(max_length=50, verbose_name='Raça/Cor')
    nacionalidade = models.CharField(max_length=50, verbose_name='Nacionalidade')
    escolaridade = models.CharField(max_length=50, verbose_name='Escolaridade')
    cep = models.CharField(max_length=8, verbose_name='CEP')
    endereco = models.CharField(max_length=255, verbose_name='Endereço')
    cidade = models.CharField(max_length=100, verbose_name='Cidade')
    uf = models.CharField(max_length=2, verbose_name='UF')
    data_inicio = models.DateField(verbose_name='Data de Início')
    ativo = models.BooleanField(default=True, verbose_name='Ativo')
    regime_contrato = models.CharField(max_length=50, verbose_name='Regime de Contrato')
    motivo_termino = models.CharField(max_length=255, blank=True, null=True, verbose_name='Motivo do Término')
    local_de_trabalho = models.CharField(max_length=100, verbose_name='Local de Trabalho')
    gestor = models.ForeignKey(
        'self', 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='subordinados',
        verbose_name='Gestor'
    )

    class Meta:
        db_table = 'funcionario'  
        verbose_name = 'Funcionario'
        verbose_name_plural = 'Funcionarios'
        ordering = ['matricula', 'data_inicio' ]

    def __str__(self):
        return self.nome

from django.db import models
from app.abstractmodel.models import TimestampableMixin

class Funcionario(TimestampableMixin):
    nome = models.CharField(max_length=150, verbose_name='Nome')
    empresa = models.ForeignKey('empresa.Empresa', verbose_name="Empresa", on_delete=models.CASCADE, null=True, blank=True )
    matricula = models.CharField(max_length=20, unique=True, verbose_name='Matrícula', null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name='CPF', null=True, blank=True)
    telefone = models.CharField(max_length=15, verbose_name='Telefone', null=True, blank=True)
    data_nascimento = models.DateField(verbose_name='Data de Nascimento', null=True, blank=True)
    genero = models.CharField(
        max_length=20, 
        choices=[
            ('M', 'Masculino'),
            ('F', 'Feminino'),
            ('O', 'Outro'),
            ('N', 'Prefiro não informar')
        ],
        verbose_name='Gênero', null=True, blank=True
    )
    raca_cor = models.CharField(max_length=50, verbose_name='Raça/Cor', null=True, blank=True)
    nacionalidade = models.CharField(max_length=50, verbose_name='Nacionalidade', null=True, blank=True)
    escolaridade = models.CharField(max_length=50, verbose_name='Escolaridade', null=True, blank=True)
    cep = models.CharField(max_length=8, verbose_name='CEP', null=True, blank=True)
    endereco = models.CharField(max_length=255, verbose_name='Endereço', null=True, blank=True)
    cidade = models.CharField(max_length=100, verbose_name='Cidade', null=True, blank=True)
    uf = models.CharField(max_length=2, verbose_name='UF', null=True, blank=True)
    data_inicio = models.DateField(verbose_name='Data de Início', null=True, blank=True)
    ativo = models.BooleanField(default=True, verbose_name='Ativo', null=True, blank=True)
    regime_contrato = models.CharField(max_length=50, verbose_name='Regime de Contrato', null=True, blank=True)
    motivo_termino = models.CharField(max_length=255, verbose_name='Motivo do Término', null=True, blank=True)
    local_de_trabalho = models.CharField(max_length=100, verbose_name='Local de Trabalho', null=True, blank=True)
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

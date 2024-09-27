from django.contrib import admin

from app.accounts.models import User
from .models import Funcionario
from ..empresa.models import Empresa, GestorRh, Organizacao

@admin.register(Funcionario)
class FuncionarioCustomAdmin(admin.ModelAdmin):
    list_display = ['nome', 'matricula', 'cpf', 'empresa', 'data_inicio', 'ativo']
    list_filter = ['empresa', 'ativo', 'genero', 'escolaridade', 'cidade', 'uf']
    search_fields = ['nome', 'matricula', 'cpf', 'empresa__nome']

    fieldsets = (
        ('Informações Pessoais', {
            'fields': ('nome', 'cpf', 'telefone', 'data_nascimento', 'genero', 'raca_cor', 'nacionalidade', 'escolaridade')
        }),
        ('Informações de Endereço', {
            'fields': ('cep', 'endereco', 'cidade', 'uf')
        }),
        ('Informações de Contrato', {
            'fields': ('empresa', 'matricula', 'data_inicio', 'regime_contrato', 'motivo_termino', 'local_de_trabalho', 'gestor')
        }),
        ('Outras Informações', {
            'fields': ('ativo',)
        }),
    )

    list_editable = ['ativo']
    ordering = ['matricula', 'data_inicio']

    def save_model(self, request, obj, form, change):
        empresa = Empresa.objects.first()
        obj.empresa = empresa
        super().save_model(request, obj, form, change)
        funcionario = obj
        usuario = User.objects.create(
            name=funcionario.nome,
            funcionario=funcionario,
            is_active=True,
            is_hr_manager=True,
            is_org_admin=True)
        GestorRh.objects.create(empresa=empresa, usuario=usuario)
        organizacao = Organizacao.objects.first()
        organizacao.usuario_admin = usuario
        organizacao.save()


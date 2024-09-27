from django.contrib import admin

from django.contrib import admin
from .models import Empresa, Porte, Organizacao, GestorRh, TabelaSalarial, ClasseSalarial

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ('razao_social', 'nome_fantasia', 'cnpj', 'cidade', 'uf', 'porte', 'organizacao')
    list_filter = ('cidade', 'uf', 'porte', 'organizacao')
    search_fields = ('razao_social', 'nome_fantasia', 'cnpj', 'cidade', 'uf')
    ordering = ('cnpj', 'cnae')

@admin.register(Porte)
class PorteAdmin(admin.ModelAdmin):
    list_display = ('porte', 'descricao')
    search_fields = ('porte',)
    ordering = ('porte',)

@admin.register(Organizacao)
class OrganizacaoAdmin(admin.ModelAdmin):
    list_display = ('organizacao_nome', 'usuario_admin')
    search_fields = ('organizacao_nome',)
    ordering = ('organizacao_nome',)

@admin.register(GestorRh)
class GestorRhAdmin(admin.ModelAdmin):
    list_display = ('empresa', 'usuario')
    list_filter = ('empresa', 'usuario')
    search_fields = ('empresa__nome_fantasia', 'usuario__username')

@admin.register(TabelaSalarial)
class TabelaSalarialAdmin(admin.ModelAdmin):
    list_display = ('versao', 'empresa', 'ativa', 'simulacao', 'data_inicio', 'data_fim')
    list_filter = ('ativa', 'simulacao', 'empresa')
    search_fields = ('versao', 'empresa__nome_fantasia')
    ordering = ('versao', 'ativa')

@admin.register(ClasseSalarial)
class ClasseSalarialAdmin(admin.ModelAdmin):
    list_display = ('nome', 'inicial', 'medio', 'final', 'tabela_salarial')
    list_filter = ('tabela_salarial',)
    search_fields = ('nome', 'tabela_salarial__versao')
    ordering = ('nome',)

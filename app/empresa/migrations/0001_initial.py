# Generated by Django 5.1.1 on 2024-09-10 20:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('razao_social', models.CharField(max_length=150, verbose_name='Razão Social')),
                ('nome_fantasia', models.CharField(max_length=150, verbose_name='Nome Fantasia')),
                ('cnpj', models.CharField(max_length=14, unique=True, verbose_name='CNPJ')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('bairro', models.CharField(max_length=100, verbose_name='Bairro')),
                ('numero', models.CharField(max_length=10, verbose_name='Número')),
                ('complemento', models.CharField(blank=True, max_length=100, verbose_name='Complemento')),
                ('logomarca', models.ImageField(blank=True, null=True, upload_to='logomarcas/', verbose_name='Logomarca')),
                ('cnae', models.CharField(max_length=10, verbose_name='CNAE')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Porte',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('porte', models.CharField(max_length=50, unique=True, verbose_name='Porte')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GestorRh',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa', verbose_name='Empresa')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='empresa',
            name='porte',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresa.porte', verbose_name='Porte'),
        ),
        migrations.CreateModel(
            name='TabelaSalarial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('versao', models.CharField(max_length=10, verbose_name='Versão')),
                ('ativa', models.BooleanField(default=True, verbose_name='Ativa')),
                ('data_inicio', models.DateField(verbose_name='Data de Início')),
                ('data_fim', models.DateField(blank=True, null=True, verbose_name='Data de Fim')),
                ('simulacao', models.BooleanField(default=False, verbose_name='Simulação')),
                ('empresa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa', verbose_name='Empresa')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ClasseSalarial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=50, verbose_name='Nome')),
                ('inicial', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Inicial')),
                ('medio', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Médio')),
                ('final', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Final')),
                ('tabela_salarial', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='empresa.tabelasalarial', verbose_name='Tabela Salarial')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
# Generated by Django 5.1.1 on 2024-09-11 11:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('empresa', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('codigo', models.CharField(max_length=20, unique=True, verbose_name='Código')),
                ('criticidade', models.CharField(max_length=50, verbose_name='Criticidade')),
                ('missao', models.TextField(verbose_name='Missão')),
                ('responsabilidade', models.TextField(verbose_name='Responsabilidade')),
                ('complexidade', models.CharField(max_length=50, verbose_name='Complexidade')),
                ('tipo', models.CharField(max_length=50, verbose_name='Tipo')),
                ('nivel', models.CharField(max_length=50, verbose_name='Nível')),
                ('eixo', models.CharField(max_length=50, verbose_name='Eixo')),
                ('carga_horaria', models.PositiveIntegerField(verbose_name='Carga Horária')),
                ('classe_salarial', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='empresa.classesalarial', verbose_name='Classe Salarial')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequisitoCertificado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('tempo', models.PositiveIntegerField(verbose_name='Tempo (meses)')),
                ('liquido', models.BooleanField(default=False, verbose_name='Tempo Líquido')),
                ('link', models.URLField(blank=True, verbose_name='Link')),
                ('obrigatorio', models.BooleanField(default=True, verbose_name='Obrigatório')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisitos_certificados', to='cargo.cargo', verbose_name='Cargo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequisitoConhecimento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('descricao', models.TextField(blank=True, verbose_name='Descrição')),
                ('obrigatorio', models.BooleanField(default=True, verbose_name='Obrigatório')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisitos_conhecimento', to='cargo.cargo', verbose_name='Cargo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequisitoEscolaridade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('nivel', models.CharField(max_length=100, verbose_name='Nível')),
                ('area', models.CharField(max_length=100, verbose_name='Área')),
                ('status', models.CharField(max_length=50, verbose_name='Status')),
                ('obrigatorio', models.BooleanField(default=True, verbose_name='Obrigatório')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisitos_escolaridade', to='cargo.cargo', verbose_name='Cargo')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='RequisitoExperiencia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True, verbose_name='Criado em')),
                ('modified_at', models.DateTimeField(auto_now=True, null=True, verbose_name='Modificado em')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('tempo', models.PositiveIntegerField(verbose_name='Tempo (meses)')),
                ('obrigatorio', models.BooleanField(default=True, verbose_name='Obrigatório')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisitos_experiencia', to='cargo.cargo', verbose_name='Cargo')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
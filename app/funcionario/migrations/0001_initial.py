# Generated by Django 5.1.1 on 2024-09-10 19:41

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
            name='Funcionario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('matricula', models.CharField(max_length=20, unique=True, verbose_name='Matrícula')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('telefone', models.CharField(blank=True, max_length=15, verbose_name='Telefone')),
                ('data_nascimento', models.DateField(verbose_name='Data de Nascimento')),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('O', 'Outro'), ('N', 'Prefiro não informar')], max_length=20, verbose_name='Gênero')),
                ('raca_cor', models.CharField(max_length=50, verbose_name='Raça/Cor')),
                ('nacionalidade', models.CharField(max_length=50, verbose_name='Nacionalidade')),
                ('escolaridade', models.CharField(max_length=50, verbose_name='Escolaridade')),
                ('cep', models.CharField(max_length=8, verbose_name='CEP')),
                ('endereco', models.CharField(max_length=255, verbose_name='Endereço')),
                ('cidade', models.CharField(max_length=100, verbose_name='Cidade')),
                ('uf', models.CharField(max_length=2, verbose_name='UF')),
                ('data_inicio', models.DateField(verbose_name='Data de Início')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo')),
                ('regime_contrato', models.CharField(max_length=50, verbose_name='Regime de Contrato')),
                ('motivo_termino', models.CharField(blank=True, max_length=255, null=True, verbose_name='Motivo do Término')),
                ('local_de_trabalho', models.CharField(max_length=100, verbose_name='Local de Trabalho')),
                ('gestor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='subordinados', to='funcionario.funcionario', verbose_name='Gestor')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuário')),
            ],
        ),
    ]

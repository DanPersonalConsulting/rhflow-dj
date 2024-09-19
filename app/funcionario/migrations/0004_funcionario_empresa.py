# Generated by Django 5.1.1 on 2024-09-18 18:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_alter_classesalarial_options_alter_empresa_options_and_more'),
        ('funcionario', '0003_alter_funcionario_options_remove_funcionario_usuario_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa'),
        ),
    ]

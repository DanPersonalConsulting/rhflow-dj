# Generated by Django 5.1.1 on 2024-09-24 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cargo',
            old_name='classe_salarial',
            new_name='classe',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='carga_horaria',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='criticidade',
        ),
        migrations.RemoveField(
            model_name='cargo',
            name='tipo',
        ),
        migrations.AddField(
            model_name='cargo',
            name='trilha',
            field=models.CharField(default=1, max_length=50, verbose_name='Trilha'),
            preserve_default=False,
        ),
    ]

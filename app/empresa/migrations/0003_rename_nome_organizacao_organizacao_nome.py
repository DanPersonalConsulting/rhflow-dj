# Generated by Django 5.1.1 on 2024-09-19 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0002_alter_classesalarial_options_alter_empresa_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='organizacao',
            old_name='nome',
            new_name='organizacao_nome',
        ),
    ]

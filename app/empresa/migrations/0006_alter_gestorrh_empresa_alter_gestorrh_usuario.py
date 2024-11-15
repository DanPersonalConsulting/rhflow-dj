# Generated by Django 5.1.1 on 2024-09-26 21:05

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empresa', '0005_alter_gestorrh_usuario'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name='gestorrh',
            name='empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='empresa.empresa', verbose_name='Empresa'),
        ),
        migrations.AlterField(
            model_name='gestorrh',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='gestores', to=settings.AUTH_USER_MODEL, verbose_name='Usuário'),
        ),
    ]

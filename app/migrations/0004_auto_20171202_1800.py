# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 20:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20171202_1759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sala',
            name='h2_Matutino',
            field=models.CharField(choices=[('Disponível', 'Disponível'), ('Reservada', 'Reservada'), ('Indisponível', 'Indisponível')], default='Disponível', max_length=12),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-10 00:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20171209_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservarmaterial',
            name='data_da_reserva',
            field=models.DateField(default=datetime.datetime(2017, 12, 9, 22, 2, 25, 854345)),
        ),
        migrations.AlterField(
            model_name='reservarsala',
            name='data_da_reserva',
            field=models.DateField(default=datetime.datetime(2017, 12, 9, 22, 2, 25, 853340)),
        ),
    ]
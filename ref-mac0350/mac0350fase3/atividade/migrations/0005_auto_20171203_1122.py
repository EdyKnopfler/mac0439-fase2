# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 13:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atividade', '0004_auto_20171203_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='atividade',
            name='data_fim',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='data_inicio',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='atividade',
            name='prazo',
            field=models.DateField(blank=True, null=True),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-12-03 14:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('analise_de_requisitos', '0002_equipe'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='analisederequisitos',
            table='analise_de_requisitos',
        ),
        migrations.AlterModelTable(
            name='equipe',
            table='equipe',
        ),
    ]

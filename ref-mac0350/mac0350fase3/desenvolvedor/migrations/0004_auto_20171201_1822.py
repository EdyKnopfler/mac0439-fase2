# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-01 18:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvedor', '0003_auto_20171129_2336'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividades',
            old_name='desenvolvedor',
            new_name='dev_id',
        ),
        migrations.RenameField(
            model_name='atividades',
            old_name='requisito',
            new_name='req_id',
        ),
        migrations.RenameField(
            model_name='equipe',
            old_name='analise_de_requisito',
            new_name='ar_id',
        ),
        migrations.RenameField(
            model_name='equipe',
            old_name='desenvolvedor',
            new_name='dev_id',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-29 23:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvedor', '0002_auto_20171128_0028'),
    ]

    operations = [
        migrations.RenameField(
            model_name='atividades',
            old_name='dev_email',
            new_name='desenvolvedor',
        ),
        migrations.RenameField(
            model_name='atividades',
            old_name='req_id',
            new_name='requisito',
        ),
        migrations.RenameField(
            model_name='equipe',
            old_name='ar_id',
            new_name='analise_de_requisito',
        ),
        migrations.RenameField(
            model_name='equipe',
            old_name='dev_email',
            new_name='desenvolvedor',
        ),
    ]

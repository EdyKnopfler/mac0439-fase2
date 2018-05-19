# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 00:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('analise_de_requisitos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisito',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('detalhes', models.TextField()),
                ('ar_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='analise_de_requisitos.AnaliseDeRequisitos')),
            ],
        ),
    ]
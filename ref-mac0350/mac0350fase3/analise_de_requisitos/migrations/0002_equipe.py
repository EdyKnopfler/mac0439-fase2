# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 20:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('desenvolvedor', '0006_auto_20171202_2026'),
        ('analise_de_requisitos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Equipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ar_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desenvolvedores', to='analise_de_requisitos.AnaliseDeRequisitos')),
                ('dev_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projetos', to='desenvolvedor.Desenvolvedor')),
            ],
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-02 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('desenvolvedor', '0007_auto_20171202_2030'),
        ('requisito', '0006_auto_20171202_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.TextField()),
                ('data_inicio', models.DateField()),
                ('data_fim', models.DateField()),
                ('prazo', models.DateField()),
                ('dev_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requisitos', to='desenvolvedor.Desenvolvedor')),
                ('req_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='desenvolvedores', to='requisito.Requisito')),
            ],
        ),
    ]
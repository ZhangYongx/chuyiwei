# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('local', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='local',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seconddomain.SecondDomain', to_field='domain', verbose_name='\u672c\u5730\u57df\u540d'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-11 09:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnsmasq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cname',
            name='cname',
            field=models.CharField(max_length=100, verbose_name='\u522b\u540d'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 05:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='create_user',
            field=models.CharField(editable=False, max_length=30, verbose_name='\u521b\u5efa\u7528\u6237'),
        ),
        migrations.AlterField(
            model_name='address',
            name='update_user',
            field=models.CharField(editable=False, max_length=30, verbose_name='\u66f4\u65b0\u7528\u6237'),
        ),
    ]

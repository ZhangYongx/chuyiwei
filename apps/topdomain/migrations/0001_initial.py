# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-24 15:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TopDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('top_domain', models.CharField(max_length=45, unique=True, verbose_name='\u9876\u7ea7\u57df\u540d')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('create_user', models.CharField(editable=False, max_length=30, verbose_name='\u521b\u5efa\u7528\u6237')),
                ('update_user', models.CharField(editable=False, max_length=30, verbose_name='\u66f4\u65b0\u7528\u6237')),
                ('remarks', models.CharField(blank=True, max_length=45, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'db_table': 'topdomain',
            },
        ),
    ]

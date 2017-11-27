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
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agt_ip', models.GenericIPAddressField(unique=True, verbose_name='\u4ee3\u7406IP')),
                ('agt_id', models.CharField(max_length=30, unique=True, verbose_name='Agent\u7f16\u53f7')),
                ('agt_version', models.CharField(default='', max_length=5, verbose_name='\u7248\u672c')),
                ('agt_states', models.IntegerField(choices=[(0, 'running'), (1, 'down'), (2, 'pause'), (3, 'unknown')], default=1, verbose_name='\u8fd0\u884c\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('create_user', models.CharField(editable=False, max_length=30, verbose_name='\u521b\u5efa\u7528\u6237')),
                ('update_user', models.CharField(editable=False, max_length=30, verbose_name='\u66f4\u65b0\u7528\u6237')),
                ('remarks', models.CharField(blank=True, max_length=45, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'db_table': 'agent',
            },
        ),
    ]

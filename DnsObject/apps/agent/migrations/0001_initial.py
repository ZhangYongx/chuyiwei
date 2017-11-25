# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-25 09:46
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
                ('agt_ip', models.CharField(max_length=39, unique=True, verbose_name='Agent IP')),
                ('agentid', models.CharField(max_length=45, unique=True, verbose_name='Agent\u7f16\u53f7')),
                ('agt_version', models.CharField(max_length=5, verbose_name='\u7248\u672c')),
                ('agt_state', models.IntegerField(choices=[(0, '\u542f\u52a8'), (1, '\u6682\u505c'), (2, '\u505c\u6b62')], verbose_name='\u72b6\u6001')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('create_user', models.CharField(max_length=30, verbose_name='\u521b\u5efa\u4eba')),
                ('update_user', models.CharField(max_length=30, verbose_name='\u66f4\u65b0\u4eba')),
                ('remarks', models.CharField(blank=True, max_length=45, null=True, verbose_name='\u5907\u6ce8')),
            ],
            options={
                'db_table': 'agent',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='agent',
            unique_together=set([('agt_ip', 'agt_version', 'agentid')]),
        ),
    ]

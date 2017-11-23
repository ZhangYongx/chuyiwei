# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-21 10:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Heartbeat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.IntegerField(unique=True, verbose_name='\u65f6\u95f4\u6233')),
                ('state', models.IntegerField(choices=[(0, '\u6b63\u5e38'), (1, '\u544a\u8b66'), (2, '\u9519\u8bef')], default=0, verbose_name='\u72b6\u6001')),
                ('agent_ip', models.GenericIPAddressField(verbose_name='Agent IP')),
                ('message', models.CharField(blank=True, max_length=10, null=True, verbose_name='\u4fe1\u606f\u4fdd\u7559')),
            ],
            options={
                'db_table': 'Heartbeat',
                'managed': True,
            },
        ),
    ]

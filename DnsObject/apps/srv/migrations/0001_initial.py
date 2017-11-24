# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-23 17:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent', '0001_initial'),
        ('seconddomain', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Srv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('srv_domain', models.CharField(max_length=45, verbose_name='\u670d\u52a1\u5730\u5740')),
                ('srv_port', models.IntegerField(blank=True, default=0, null=True, verbose_name='\u7aef\u53e3')),
                ('priority', models.IntegerField(default=10, verbose_name='\u4f18\u5148\u7ea7')),
                ('weight', models.IntegerField(default=10, verbose_name='\u6743\u91cd')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('create_user', models.CharField(editable=False, max_length=30, verbose_name='\u521b\u5efa\u7528\u6237')),
                ('update_user', models.CharField(editable=False, max_length=30, verbose_name='\u66f4\u65b0\u7528\u6237')),
                ('remarks', models.CharField(blank=True, max_length=45, null=True, verbose_name='\u5907\u6ce8')),
                ('agentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Agent', to_field='agentid', verbose_name='Agent\u7f16\u53f7')),
                ('domain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='seconddomain.SecondDomain', to_field='domain', verbose_name='\u57df\u540d')),
            ],
            options={
                'db_table': 'srv',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='srv',
            unique_together=set([('srv_domain', 'agentid')]),
        ),
    ]

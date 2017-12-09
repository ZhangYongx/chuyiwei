# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-09 10:37
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('old_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='\u539fIP')),
                ('start_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='\u8d77\u59cbIP')),
                ('end_ip', models.GenericIPAddressField(blank=True, null=True, verbose_name='\u7ed3\u675fIP')),
                ('new_ip', models.GenericIPAddressField(verbose_name='\u65b0IP')),
                ('ipmask', models.GenericIPAddressField(blank=True, null=True, verbose_name='\u63a9\u7801')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('create_user', models.CharField(editable=False, max_length=30, verbose_name='\u521b\u5efa\u7528\u6237')),
                ('update_user', models.CharField(editable=False, max_length=30, verbose_name='\u66f4\u65b0\u7528\u6237')),
                ('remarks', models.CharField(blank=True, max_length=45, null=True, verbose_name='\u5907\u6ce8')),
                ('agentid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agent.Agent', to_field='agentid', verbose_name='Agent\u7f16\u53f7')),
            ],
            options={
                'db_table': 'alias',
                'managed': True,
            },
        ),
        migrations.AlterUniqueTogether(
            name='alias',
            unique_together=set([('new_ip', 'agentid')]),
        ),
    ]

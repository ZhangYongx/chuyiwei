# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-14 06:36
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('area', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resolv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resolv_ip', models.GenericIPAddressField(verbose_name='IP')),
                ('resolv_port', models.IntegerField(blank=True, null=True, verbose_name='\u7aef\u53e3')),
                ('remarks', models.CharField(blank=True, max_length=45, null=True, verbose_name='\u5907\u6ce8')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='\u66f4\u65b0\u65f6\u95f4')),
                ('create_user', models.CharField(default='now user', editable=False, max_length=30, verbose_name='\u521b\u5efa\u7528\u6237')),
                ('update_user', models.CharField(default='now user', editable=False, max_length=30, verbose_name='\u66f4\u65b0\u7528\u6237')),
                ('area_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='area.Area', to_field='name', verbose_name='\u533a\u57df')),
            ],
            options={
                'db_table': 'resolv',
            },
        ),
        migrations.AlterUniqueTogether(
            name='resolv',
            unique_together=set([('resolv_ip', 'area_name')]),
        ),
    ]

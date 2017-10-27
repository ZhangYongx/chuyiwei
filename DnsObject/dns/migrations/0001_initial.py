# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.6 on 2017-10-20 03:00
=======
# Generated by Django 1.11.6 on 2017-10-24 09:22
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaid', models.IntegerField()),
                ('domain_name', models.CharField(blank=True, max_length=45, null=True)),
                ('ip', models.IntegerField(blank=True, db_column='IP', null=True)),
                ('create_time', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
                ('updateuser', models.CharField(max_length=45, null=True)),
=======
                ('domain', models.CharField(blank=True, max_length=45, null=True)),
                ('ip', models.CharField(blank=True, max_length=32, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=20, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaid', models.IntegerField()),
                ('agentip', models.IntegerField(blank=True, db_column='agentIp', null=True)),
                ('agentversion', models.CharField(blank=True, db_column='agentVersion', max_length=45, null=True)),
                ('agentstatu', models.CharField(blank=True, db_column='agentStatu', max_length=45, null=True)),
=======
                ('agent_ip', models.CharField(blank=True, max_length=32, null=True)),
                ('agent_version', models.CharField(blank=True, max_length=45, null=True)),
                ('agent_statu', models.CharField(blank=True, max_length=45, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'agent',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Alias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaid', models.IntegerField()),
                ('oldip', models.CharField(blank=True, db_column='oldIp', max_length=45, null=True)),
                ('startipendip', models.IntegerField(blank=True, db_column='startIpEndIp', null=True)),
                ('newip', models.IntegerField(blank=True, db_column='newIp', null=True)),
                ('mask', models.CharField(blank=True, max_length=45, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
                ('updateuser', models.CharField(blank=True, db_column='updateUser', max_length=45, null=True)),
=======
                ('old_ip', models.CharField(blank=True, max_length=45, null=True)),
                ('start_ip', models.CharField(blank=True, max_length=32, null=True)),
                ('end_ip', models.CharField(blank=True, max_length=32, null=True)),
                ('new_ip', models.CharField(blank=True, max_length=32, null=True)),
                ('mask', models.CharField(blank=True, max_length=45, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=45, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'alias',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaname', models.CharField(blank=True, db_column='areaName', max_length=45, null=True)),
=======
                ('area', models.CharField(blank=True, max_length=45, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('responsible', models.CharField(blank=True, max_length=45, null=True)),
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'area',
                'managed': False,
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='Cname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('areaid', models.IntegerField()),
                ('cnamename', models.CharField(blank=True, db_column='cnameName', max_length=45, null=True)),
                ('domainname', models.CharField(blank=True, db_column='domainName', max_length=45, null=True)),
                ('ttl', models.IntegerField(blank=True, db_column='TTL', null=True)),
=======
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('content_type_id', models.IntegerField()),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.IntegerField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.IntegerField()),
                ('is_active', models.IntegerField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('group_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('permission_id', models.IntegerField()),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Cname',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('target_domain', models.CharField(blank=True, max_length=45, null=True)),
                ('domain', models.CharField(blank=True, max_length=45, null=True)),
                ('ttl', models.IntegerField(blank=True, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('create_time', models.CharField(blank=True, max_length=45, null=True)),
                ('update_time', models.CharField(blank=True, max_length=45, null=True)),
                ('update_user', models.CharField(blank=True, max_length=45, null=True)),
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'cname',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='ComputerRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('computername', models.CharField(blank=True, db_column='computerName', max_length=45, null=True)),
=======
                ('computer_name', models.CharField(blank=True, max_length=45, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('responsible', models.CharField(blank=True, max_length=45, null=True)),
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'computer_room',
                'managed': False,
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='DoaminName',
=======
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
                ('content_type_id', models.IntegerField(blank=True, null=True)),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Doamin',
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('sid', models.IntegerField(blank=True, null=True)),
                ('multilevel', models.CharField(blank=True, max_length=45, null=True)),
<<<<<<< HEAD
                ('fulldomainname', models.CharField(blank=True, db_column='fullDomainName', max_length=45, null=True)),
                ('analytictype', models.CharField(blank=True, db_column='analyticType', max_length=45, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
                ('createuser', models.CharField(blank=True, db_column='createUser', max_length=30, null=True)),
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'doamin_name',
=======
                ('full_domain', models.CharField(blank=True, max_length=45, null=True)),
                ('analytic_type', models.CharField(blank=True, max_length=45, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('create_user', models.CharField(blank=True, max_length=30, null=True)),
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'doamin',
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                'managed': False,
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='FDomainName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domainname', models.CharField(blank=True, db_column='domainName', max_length=45, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
                ('createuser', models.CharField(blank=True, db_column='createUser', max_length=45, null=True)),
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'f_domain_name',
=======
            name='FDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(blank=True, max_length=45, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('create_user', models.CharField(blank=True, max_length=45, null=True)),
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'f_domain',
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='HostRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaid', models.IntegerField()),
                ('domainname', models.CharField(blank=True, db_column='domainName', max_length=45, null=True)),
                ('ip', models.IntegerField(blank=True, db_column='IP', null=True)),
                ('ttl', models.CharField(blank=True, db_column='TTL', max_length=45, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
                ('updateuser', models.CharField(blank=True, db_column='updateUser', max_length=30, null=True)),
=======
                ('domain', models.CharField(blank=True, max_length=45, null=True)),
                ('ip', models.CharField(blank=True, max_length=32, null=True)),
                ('ttl', models.CharField(blank=True, max_length=45, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=30, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'host-record',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ipinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.IntegerField(blank=True, null=True)),
<<<<<<< HEAD
                ('computerid', models.IntegerField(blank=True, db_column='computerId', null=True)),
=======
                ('cname_id', models.IntegerField(blank=True, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('remark', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'ipinfo',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaid', models.IntegerField()),
                ('domainname', models.CharField(blank=True, db_column='domainName', max_length=45, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
                ('updateuser', models.CharField(blank=True, db_column='updateUser', max_length=45, null=True)),
=======
                ('local', models.CharField(blank=True, max_length=45, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=45, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'local',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Mx',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaid', models.IntegerField()),
                ('domainname', models.CharField(blank=True, db_column='domainName', max_length=45, null=True)),
                ('mailname', models.CharField(blank=True, db_column='mailName', max_length=45, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
                ('updateuser', models.CharField(blank=True, db_column='updateUser', max_length=45, null=True)),
=======
                ('domain', models.CharField(blank=True, max_length=45, null=True)),
                ('mail_domain', models.CharField(blank=True, max_length=45, null=True)),
                ('preference', models.IntegerField(blank=True, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=45, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'mx',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Ptr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaid', models.IntegerField()),
                ('ip', models.IntegerField(blank=True, db_column='IP', null=True)),
                ('domainname', models.CharField(blank=True, db_column='domainName', max_length=45, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
                ('updateuser', models.CharField(blank=True, db_column='updateUser', max_length=45, null=True)),
=======
                ('ip', models.CharField(blank=True, max_length=32, null=True)),
                ('domain', models.CharField(blank=True, max_length=45, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=45, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'ptr',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Resolv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaid', models.IntegerField()),
                ('ip', models.IntegerField(blank=True, db_column='IP', null=True)),
=======
                ('ip', models.IntegerField(blank=True, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('port', models.IntegerField(blank=True, null=True)),
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'resolv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
<<<<<<< HEAD
            name='SDomainName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField(blank=True, null=True)),
                ('domainname', models.CharField(blank=True, db_column='domainName', max_length=45, null=True)),
                ('fulldomainname', models.CharField(blank=True, db_column='fullDomainName', max_length=45, null=True)),
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
                ('createuser', models.CharField(blank=True, db_column='createUser', max_length=30, null=True)),
            ],
            options={
                'db_table': 's_domain_name',
=======
            name='SDomain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fid', models.IntegerField(blank=True, null=True)),
                ('domain', models.CharField(blank=True, max_length=45, null=True)),
                ('full_domain', models.CharField(blank=True, max_length=45, null=True)),
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('create_user', models.CharField(blank=True, max_length=30, null=True)),
            ],
            options={
                'db_table': 's_domain',
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Servere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaid', models.IntegerField()),
                ('domain_name', models.CharField(blank=True, max_length=45, null=True)),
                ('reverseip', models.IntegerField(blank=True, db_column='reverseIp', null=True)),
                ('nsip', models.IntegerField(blank=True, db_column='nsIp', null=True)),
                ('nsport', models.CharField(blank=True, db_column='nsPort', max_length=45, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
                ('updateuser', models.CharField(blank=True, db_column='updateUser', max_length=45, null=True)),
=======
                ('domain', models.CharField(blank=True, max_length=45, null=True)),
                ('server_ptr', models.CharField(blank=True, max_length=32, null=True)),
                ('ip', models.CharField(blank=True, max_length=32, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=45, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'servere',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Srv',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaid', models.IntegerField()),
                ('domainname', models.CharField(blank=True, db_column='domainName', max_length=45, null=True)),
                ('serveraddr', models.CharField(blank=True, db_column='serverAddr', max_length=45, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('priority', models.CharField(blank=True, max_length=45, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
                ('updateuser', models.CharField(blank=True, db_column='updateUser', max_length=45, null=True)),
=======
                ('domain', models.CharField(blank=True, max_length=45, null=True)),
                ('server_domain', models.CharField(blank=True, max_length=45, null=True)),
                ('port', models.IntegerField(blank=True, null=True)),
                ('priority', models.IntegerField(blank=True, null=True)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('update_user', models.CharField(blank=True, max_length=45, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'srv',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Txt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('areaid', models.IntegerField()),
                ('domainname', models.CharField(blank=True, db_column='domainName', max_length=45, null=True)),
                ('text', models.CharField(blank=True, max_length=45, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
                ('updatetime', models.DateTimeField(blank=True, db_column='updateTime', null=True)),
=======
                ('domain', models.CharField(blank=True, max_length=45, null=True)),
                ('text', models.CharField(blank=True, max_length=45, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('update_user', models.CharField(blank=True, max_length=45, null=True)),
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'txt',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
<<<<<<< HEAD
                ('username', models.CharField(blank=True, db_column='userName', max_length=45, null=True)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('permission', models.CharField(blank=True, max_length=45, null=True)),
                ('createtime', models.DateTimeField(blank=True, db_column='createTime', null=True)),
=======
                ('username', models.CharField(blank=True, max_length=45, null=True)),
                ('password', models.CharField(blank=True, max_length=45, null=True)),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('permission', models.CharField(blank=True, max_length=45, null=True)),
>>>>>>> 95fd0ef0dff3f92be117f777f9cf164515ec7af6
                ('remarks', models.CharField(blank=True, max_length=45, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]

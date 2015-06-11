# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0014_auto_20150610_1419'),
        ('operating', '0002_responsemail'),
    ]

    operations = [
        migrations.CreateModel(
            name='CDNServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(unique=True, max_length=45)),
                ('ip', models.GenericIPAddressField()),
                ('port', models.IntegerField()),
                ('hostname', models.CharField(max_length=45)),
                ('home', models.CharField(max_length=60)),
                ('cdn_url', models.CharField(max_length=256)),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
            options={
                'db_table': 'config_cdn_server',
            },
        ),
        migrations.CreateModel(
            name='Notify',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(unique=True, max_length=45)),
                ('title', models.CharField(max_length=256)),
                ('content', models.TextField()),
                ('is_display', models.IntegerField()),
                ('link', models.CharField(max_length=256)),
                ('hostname', models.CharField(max_length=45)),
                ('channel', models.IntegerField()),
                ('platform', models.CharField(max_length=45)),
                ('world_id', models.IntegerField()),
                ('notify_url', models.CharField(max_length=256)),
                ('seqid', models.IntegerField()),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
            options={
                'ordering': ['seqid'],
            },
        ),
        migrations.AlterModelOptions(
            name='responsemail',
            options={'ordering': ['-pub_date']},
        ),
    ]

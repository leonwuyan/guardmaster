# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0017_auto_20150818_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.IntegerField()),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
        ),
        migrations.CreateModel(
            name='HostName',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=45)),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=45)),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
        ),
        migrations.CreateModel(
            name='UpLoadWorkOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=45)),
                ('platform', models.CharField(max_length=45)),
                ('channel', models.IntegerField()),
                ('version', models.CharField(max_length=45)),
                ('progress', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('stop_date', models.DateTimeField(null=True, blank=True)),
                ('server', models.CharField(max_length=45)),
                ('user', models.CharField(max_length=45)),
                ('result', models.CharField(max_length=255)),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]

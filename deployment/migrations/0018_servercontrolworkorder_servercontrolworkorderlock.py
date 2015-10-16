# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0021_auto_20151015_1442'),
        ('deployment', '0017_ciwp'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerControlWorkOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server', models.CharField(max_length=45)),
                ('stage', models.CharField(max_length=45)),
                ('release', models.CharField(max_length=45)),
                ('ciwp', models.IntegerField()),
                ('version', models.CharField(max_length=45)),
                ('progress', models.IntegerField()),
                ('start_date', models.DateTimeField()),
                ('stop_date', models.DateTimeField(null=True, blank=True)),
                ('user', models.CharField(max_length=45)),
                ('result', models.CharField(max_length=255)),
                ('status', models.IntegerField()),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ServerControlWorkOrderLock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('server', models.CharField(max_length=45)),
                ('status', models.IntegerField()),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
        ),
    ]

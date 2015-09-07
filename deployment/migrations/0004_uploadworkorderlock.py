# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0018_auto_20150907_2005'),
        ('deployment', '0003_auto_20150907_1928'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpLoadWorkOrderLock',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=45)),
                ('platform', models.CharField(max_length=45)),
                ('channel', models.IntegerField()),
                ('status', models.IntegerField()),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0004_uploadworkorderlock'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uploadworkorderlock',
            name='id',
        ),
        migrations.AlterField(
            model_name='uploadworkorderlock',
            name='channel',
            field=models.IntegerField(primary_key=True),
        ),
        migrations.AlterField(
            model_name='uploadworkorderlock',
            name='hostname',
            field=models.CharField(max_length=45, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='uploadworkorderlock',
            name='panel',
            field=models.ForeignKey(to='detection.Panel', primary_key=True),
        ),
        migrations.AlterField(
            model_name='uploadworkorderlock',
            name='platform',
            field=models.CharField(max_length=45, primary_key=True),
        ),
    ]

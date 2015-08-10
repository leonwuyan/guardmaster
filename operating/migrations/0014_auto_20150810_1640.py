# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0013_auto_20150714_2052'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notify',
            name='notify_url',
        ),
        migrations.AlterField(
            model_name='notify',
            name='channel',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='notify',
            name='world_id',
            field=models.CharField(max_length=128),
        ),
    ]

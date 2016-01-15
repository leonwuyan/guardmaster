# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0025_auto_20160112_1753'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='serverconfigorder',
            name='db_list',
        ),
        migrations.AddField(
            model_name='serverconfigorder',
            name='db_list',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='serverconfigorder',
            name='hs_free_list',
        ),
        migrations.AddField(
            model_name='serverconfigorder',
            name='hs_free_list',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='serverconfigorder',
            name='hs_list',
        ),
        migrations.AddField(
            model_name='serverconfigorder',
            name='hs_list',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='serverconfigorder',
            name='ps_list',
        ),
        migrations.AddField(
            model_name='serverconfigorder',
            name='ps_list',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]

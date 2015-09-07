# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0002_hostname_dir_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadworkorder',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uploadworkorder',
            name='update_list',
            field=models.TextField(null=True, blank=True),
        ),
    ]

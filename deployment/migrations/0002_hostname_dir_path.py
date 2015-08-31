# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostname',
            name='dir_path',
            field=models.CharField(default='myci', max_length=45),
            preserve_default=False,
        ),
    ]

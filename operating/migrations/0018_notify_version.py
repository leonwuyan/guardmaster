# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0017_auto_20151106_1714'),
    ]

    operations = [
        migrations.AddField(
            model_name='notify',
            name='version',
            field=models.CharField(default='1.1.0.0', max_length=128),
            preserve_default=False,
        ),
    ]

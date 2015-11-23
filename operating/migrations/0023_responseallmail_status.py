# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0022_auto_20151120_0326'),
    ]

    operations = [
        migrations.AddField(
            model_name='responseallmail',
            name='status',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0025_gmorder'),
    ]

    operations = [
        migrations.AddField(
            model_name='gmorder',
            name='remarks',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]

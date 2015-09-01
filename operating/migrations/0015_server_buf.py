# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0014_auto_20150810_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='buf',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]

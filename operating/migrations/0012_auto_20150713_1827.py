# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0011_auto_20150708_0907'),
    ]

    operations = [
        migrations.AddField(
            model_name='notify',
            name='end',
            field=models.DateField(default='2015-12-24'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notify',
            name='start',
            field=models.DateField(default='2015-06-27'),
            preserve_default=False,
        ),
    ]

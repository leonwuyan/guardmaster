# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0012_auto_20150713_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='end',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='notify',
            name='start',
            field=models.DateTimeField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0021_auto_20151119_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='responseallmail',
            name='end_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='responseallmail',
            name='start_date',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0026_gmorder_remarks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='world_id',
            field=models.CharField(max_length=256),
        ),
    ]

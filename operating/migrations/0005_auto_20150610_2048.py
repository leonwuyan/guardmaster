# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0004_remove_notify_label'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='link',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]

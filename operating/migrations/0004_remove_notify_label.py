# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0003_auto_20150610_1419'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notify',
            name='label',
        ),
    ]

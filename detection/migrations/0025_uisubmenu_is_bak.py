# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0024_auto_20151214_1558'),
    ]

    operations = [
        migrations.AddField(
            model_name='uisubmenu',
            name='is_bak',
            field=models.BooleanField(default=False),
        ),
    ]

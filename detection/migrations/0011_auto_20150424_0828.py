# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0010_auto_20150424_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uisubmenu',
            name='url',
            field=models.CharField(unique=True, max_length=200, db_index=True),
        ),
    ]

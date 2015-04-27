# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0004_auto_20150422_0343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uisubmenu',
            name='db_name',
            field=models.CharField(max_length=45),
        ),
    ]

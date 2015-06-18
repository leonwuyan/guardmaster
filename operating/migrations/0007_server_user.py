# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0006_auto_20150618_1129'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='user',
            field=models.CharField(default='act', max_length=45),
            preserve_default=False,
        ),
    ]

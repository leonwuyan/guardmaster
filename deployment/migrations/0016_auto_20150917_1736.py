# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0015_tpltemplate_saved_path'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tplitem',
            name='item_desc',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]

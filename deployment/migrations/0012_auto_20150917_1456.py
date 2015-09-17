# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0011_tplitem_tpl_template'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tplitem',
            name='editable',
            field=models.IntegerField(),
        ),
    ]

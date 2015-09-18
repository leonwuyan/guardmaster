# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0013_auto_20150917_1628'),
    ]

    operations = [
        migrations.AddField(
            model_name='tpltemplate',
            name='out_dir',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]

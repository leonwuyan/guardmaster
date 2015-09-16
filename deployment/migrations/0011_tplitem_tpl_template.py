# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0010_auto_20150916_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='tplitem',
            name='tpl_template',
            field=models.ForeignKey(default=1, to='deployment.TplTemplate'),
            preserve_default=False,
        ),
    ]

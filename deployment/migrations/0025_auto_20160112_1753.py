# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0024_serverconfigorder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tplitem',
            name='tpl_template',
        ),
        migrations.DeleteModel(
            name='TplItem',
        ),
        migrations.DeleteModel(
            name='TplTemplate',
        ),
    ]

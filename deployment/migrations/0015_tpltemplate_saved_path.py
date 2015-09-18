# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0014_tpltemplate_out_dir'),
    ]

    operations = [
        migrations.AddField(
            model_name='tpltemplate',
            name='saved_path',
            field=models.CharField(default='', max_length=45),
            preserve_default=False,
        ),
    ]

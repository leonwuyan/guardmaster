# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0028_auto_20160115_1958'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='channel',
            options={'ordering': ['label']},
        ),
        migrations.AddField(
            model_name='servercontrolworkorder',
            name='output',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
    ]

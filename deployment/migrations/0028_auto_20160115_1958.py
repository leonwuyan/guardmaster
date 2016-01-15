# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0027_auto_20160115_1516'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='serverconfigorder',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='serverconfigorder',
            name='label',
        ),
    ]

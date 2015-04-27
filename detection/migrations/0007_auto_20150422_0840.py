# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0006_auto_20150422_0607'),
    ]

    operations = [
        migrations.RenameField(
            model_name='panel',
            old_name='db_name',
            new_name='db_aliases',
        ),
        migrations.AlterField(
            model_name='uicolmap',
            name='col_type',
            field=models.CharField(blank=True, max_length=45, null=True, choices=[(b'date', b'date'), (b'channelist', b'channelist'), (b'zonelist', b'zonelist')]),
        ),
    ]

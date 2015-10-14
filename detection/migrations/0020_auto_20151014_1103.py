# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0019_auto_20151014_1059'),
    ]

    operations = [
        migrations.RenameField(
            model_name='panel',
            old_name='start_time',
            new_name='start_date',
        ),
    ]

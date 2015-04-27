# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0008_auto_20150423_1019'),
    ]

    operations = [
        migrations.RenameField(
            model_name='panel',
            old_name='group',
            new_name='groups',
        ),
        migrations.RenameField(
            model_name='uimainmenu',
            old_name='group',
            new_name='groups',
        ),
    ]

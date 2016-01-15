# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0026_auto_20160115_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='databin',
            name='panel',
        ),
        migrations.DeleteModel(
            name='DataBin',
        ),
    ]

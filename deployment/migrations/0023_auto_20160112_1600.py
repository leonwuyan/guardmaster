# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0022_auto_20160111_1558'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotstart',
            name='panel',
        ),
        migrations.DeleteModel(
            name='HotStart',
        ),
    ]

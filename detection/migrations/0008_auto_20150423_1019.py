# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('detection', '0007_auto_20150422_0840'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='panel',
            name='group',
        ),
        migrations.AddField(
            model_name='panel',
            name='group',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]

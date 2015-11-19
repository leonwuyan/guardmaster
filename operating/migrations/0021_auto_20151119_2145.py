# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0020_responseallmail_version'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='responseallmail',
            name='response_id',
        ),
        migrations.AddField(
            model_name='responseallmail',
            name='response_list',
            field=models.CharField(default='', max_length=256),
            preserve_default=False,
        ),
    ]

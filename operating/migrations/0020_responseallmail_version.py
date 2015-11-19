# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0019_responseallmail'),
    ]

    operations = [
        migrations.AddField(
            model_name='responseallmail',
            name='version',
            field=models.CharField(default='.*', max_length=45),
            preserve_default=False,
        ),
    ]

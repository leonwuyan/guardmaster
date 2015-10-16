# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0018_servercontrolworkorder_servercontrolworkorderlock'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servercontrolworkorder',
            name='ciwp',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='servercontrolworkorder',
            name='version',
            field=models.IntegerField(),
        ),
    ]

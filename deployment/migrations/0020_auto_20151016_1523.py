# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0019_auto_20151015_1508'),
    ]

    operations = [
        migrations.RenameField(
            model_name='servercontrolworkorder',
            old_name='ciwp',
            new_name='parameter1',
        ),
        migrations.RenameField(
            model_name='servercontrolworkorder',
            old_name='release',
            new_name='parameter2',
        ),
        migrations.RenameField(
            model_name='servercontrolworkorder',
            old_name='stage',
            new_name='parameter3',
        ),
        migrations.RemoveField(
            model_name='servercontrolworkorder',
            name='version',
        ),
        migrations.AddField(
            model_name='servercontrolworkorder',
            name='parameter4',
            field=models.CharField(default='0', max_length=45),
            preserve_default=False,
        ),
    ]

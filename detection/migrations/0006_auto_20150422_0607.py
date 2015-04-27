# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0005_auto_20150422_0344'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uicolmap',
            old_name='db_col',
            new_name='col_name',
        ),
        migrations.RemoveField(
            model_name='uisubmenu',
            name='db_name',
        ),
        migrations.AddField(
            model_name='panel',
            name='db_name',
            field=models.CharField(default=1, max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uisubmenu',
            name='table_name',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='panel',
            name='label',
            field=models.CharField(unique=True, max_length=45),
        ),
        migrations.AlterField(
            model_name='uicolmap',
            name='col_type',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='uisubmenu',
            name='category',
            field=models.CharField(max_length=45, null=True, blank=True),
        ),
    ]

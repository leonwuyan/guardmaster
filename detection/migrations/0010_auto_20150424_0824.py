# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0009_auto_20150423_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uisubmenu',
            name='main_menu',
            field=models.ForeignKey(blank=True, to='detection.UIMainMenu', null=True),
        ),
    ]

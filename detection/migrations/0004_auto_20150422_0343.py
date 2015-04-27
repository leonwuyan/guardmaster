# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0003_auto_20150422_0325'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uicolmap',
            options={'ordering': ['sub_menu', 'seqid']},
        ),
        migrations.AlterModelOptions(
            name='uisubmenu',
            options={'ordering': ['main_menu', 'seqid']},
        ),
        migrations.AddField(
            model_name='uisubmenu',
            name='db_name',
            field=models.CharField(default=b'1', max_length=45),
        ),
    ]

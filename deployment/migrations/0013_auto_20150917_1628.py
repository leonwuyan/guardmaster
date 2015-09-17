# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0012_auto_20150917_1456'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tplitem',
            options={'ordering': ['seqid', 'module_seqid']},
        ),
    ]

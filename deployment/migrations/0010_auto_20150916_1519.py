# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0009_tplitem_tpltemplate'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tplitem',
            old_name='module_sequd',
            new_name='module_seqid',
        ),
    ]

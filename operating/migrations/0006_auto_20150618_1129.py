# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0005_auto_20150610_2048'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='notify',
            options={'ordering': ['hostname', 'channel', 'platform', 'seqid']},
        ),
        migrations.AlterField(
            model_name='responsemail',
            name='response_id',
            field=models.BigIntegerField(),
        ),
    ]

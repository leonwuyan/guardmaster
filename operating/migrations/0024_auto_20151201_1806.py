# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0023_responseallmail_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='server',
            name='server_type',
            field=models.CharField(max_length=45, choices=[(b'world', 'World Server'), (b'normal', 'Normal Server'), (b'update', 'Update Server'), (b'cdn', 'CDN Server'), (b'redundance', 'Redundance Update Server'), (b'dir', 'Dir Server'), (b'all', 'GameAll Server'), (b'zone', 'Zone Server')]),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0007_server_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='cdn_url',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='server',
            name='server_type',
            field=models.CharField(default='dir', max_length=45, choices=[(b'cdn', 'CDN Server'), (b'normal', 'Normal Server'), (b'dir', 'Dir Server')]),
            preserve_default=False,
        ),
    ]

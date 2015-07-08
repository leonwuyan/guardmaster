# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0010_auto_20150706_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notify',
            name='channel',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='notify',
            name='world_id',
            field=models.CharField(max_length=45),
        ),
        migrations.AlterField(
            model_name='server',
            name='server_type',
            field=models.CharField(max_length=45, choices=[(b'cdn', 'CDN Server'), (b'dir', 'Dir Server'), (b'normal', 'Normal Server'), (b'update', 'Update Server')]),
        ),
    ]

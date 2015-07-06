# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0009_auto_20150630_1603'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cdnserver',
            name='panel',
        ),
        migrations.AddField(
            model_name='notify',
            name='image_height',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notify',
            name='image_width',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='server',
            name='server_type',
            field=models.CharField(max_length=45, choices=[(b'cdn', 'CDN Server'), (b'update', 'Update Server'), (b'dir', 'Dir Server'), (b'normal', 'Normal Server')]),
        ),
        migrations.DeleteModel(
            name='CDNServer',
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0015_server_buf'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='db_host',
            field=models.GenericIPAddressField(default='127.0.0.1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='db_password',
            field=models.CharField(default='8791act@b7', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='db_user',
            field=models.CharField(default='91act', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='inetip',
            field=models.GenericIPAddressField(default='192.168.1.90'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='perform',
            field=models.CharField(default='4core 32G 220G(SSD)', max_length=45),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='server',
            name='world_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='server',
            name='server_type',
            field=models.CharField(max_length=45, choices=[(b'normal', 'Normal Server'), (b'update', 'Update Server'), (b'cdn', 'CDN Server'), (b'all', 'GameAll Server'), (b'dir', 'Dir Server'), (b'zone', 'Zone Server'), (b'world', 'World Server')]),
        ),
    ]

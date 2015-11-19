# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0018_notify_version'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseAllMail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=45)),
                ('content', models.CharField(max_length=256)),
                ('guardmaster', models.CharField(max_length=45)),
                ('zone', models.CharField(max_length=256)),
                ('accessory', models.TextField()),
                ('response_id', models.BigIntegerField()),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('server', models.ForeignKey(to='operating.Server')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]

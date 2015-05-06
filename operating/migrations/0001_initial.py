# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0012_auto_20150505_1143'),
    ]

    operations = [
        migrations.CreateModel(
            name='Server',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(unique=True, max_length=45)),
                ('ip', models.GenericIPAddressField()),
                ('port', models.IntegerField()),
                ('hostname', models.CharField(max_length=45)),
                ('home', models.CharField(max_length=60)),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
            options={
                'db_table': 'config_server',
            },
        ),
    ]

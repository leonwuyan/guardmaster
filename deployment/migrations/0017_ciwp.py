# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0020_auto_20151014_1103'),
        ('deployment', '0016_auto_20150917_1736'),
    ]

    operations = [
        migrations.CreateModel(
            name='CIWP',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=45)),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
        ),
    ]

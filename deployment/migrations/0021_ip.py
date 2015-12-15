# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0026_auto_20151214_2148'),
        ('deployment', '0020_auto_20151016_1523'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ip',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.GenericIPAddressField()),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
        ),
    ]

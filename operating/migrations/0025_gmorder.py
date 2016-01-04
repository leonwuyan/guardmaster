# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0024_auto_20151201_1806'),
    ]

    operations = [
        migrations.CreateModel(
            name='GmOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=64)),
                ('param_count', models.IntegerField()),
                ('is_work', models.IntegerField(default=0)),
                ('seqid', models.IntegerField()),
            ],
            options={
                'ordering': ['seqid'],
            },
        ),
    ]

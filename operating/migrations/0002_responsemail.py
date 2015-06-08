# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResponseMail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=45)),
                ('content', models.CharField(max_length=256)),
                ('guardmaster', models.CharField(max_length=45)),
                ('uid', models.IntegerField()),
                ('accessory', models.TextField()),
                ('response_id', models.IntegerField()),
                ('pub_date', models.DateTimeField()),
                ('server', models.ForeignKey(to='operating.Server')),
            ],
        ),
    ]

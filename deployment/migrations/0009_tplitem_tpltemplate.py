# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deployment', '0008_uploadworkorderlock'),
    ]

    operations = [
        migrations.CreateModel(
            name='TplItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('module_name', models.CharField(max_length=45)),
                ('module_times', models.IntegerField()),
                ('module_sequd', models.IntegerField()),
                ('item_name', models.CharField(max_length=45)),
                ('editable', models.BooleanField()),
                ('item_desc', models.CharField(max_length=255)),
                ('item_default', models.CharField(max_length=255, null=True, blank=True)),
                ('item_valuelist', models.TextField(null=True, blank=True)),
                ('seqid', models.IntegerField()),
            ],
            options={
                'ordering': ['seqid'],
                'db_table': 'tpl_item',
            },
        ),
        migrations.CreateModel(
            name='TplTemplate',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tpl_type', models.CharField(max_length=45)),
                ('out_file_type', models.CharField(max_length=45)),
                ('out_name_mask', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'tpl_template',
            },
        ),
    ]

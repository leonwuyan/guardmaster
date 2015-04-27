# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('detection', '0002_auto_20150420_0923'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=45)),
                ('group', models.ForeignKey(to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='UIColMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=45)),
                ('db_col', models.CharField(max_length=45)),
                ('col_type', models.CharField(max_length=45, null=True)),
                ('seqid', models.IntegerField()),
            ],
            options={
                'ordering': ['seqid'],
                'db_table': 'ui_col_map',
            },
        ),
        migrations.CreateModel(
            name='UIMainMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=45)),
                ('seqid', models.IntegerField()),
                ('group', models.ManyToManyField(to='auth.Group')),
            ],
            options={
                'ordering': ['seqid'],
                'db_table': 'ui_main_menu',
            },
        ),
        migrations.CreateModel(
            name='UISubMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=45)),
                ('url', models.CharField(max_length=200)),
                ('category', models.CharField(max_length=45, null=True)),
                ('seqid', models.IntegerField()),
                ('main_menu', models.ForeignKey(to='detection.UIMainMenu')),
            ],
            options={
                'ordering': ['seqid'],
                'db_table': 'ui_sub_menu',
            },
        ),
        migrations.AddField(
            model_name='uicolmap',
            name='sub_menu',
            field=models.ForeignKey(to='detection.UISubMenu'),
        ),
    ]

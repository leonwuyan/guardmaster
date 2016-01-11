# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0027_auto_20160111_1558'),
        ('deployment', '0021_ip'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataBin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=256)),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
        ),
        migrations.CreateModel(
            name='HotStart',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=256)),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
        ),
        migrations.CreateModel(
            name='ProcessServer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=256)),
                ('panel', models.ForeignKey(to='detection.Panel')),
            ],
        ),
        migrations.AddField(
            model_name='servercontrolworkorder',
            name='parameter5',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='servercontrolworkorder',
            name='parameter1',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='servercontrolworkorder',
            name='parameter2',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='servercontrolworkorder',
            name='parameter3',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='servercontrolworkorder',
            name='parameter4',
            field=models.CharField(max_length=256, null=True, blank=True),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0027_auto_20160111_1558'),
        ('deployment', '0023_auto_20160112_1600'),
    ]

    operations = [
        migrations.CreateModel(
            name='ServerConfigOrder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('label', models.CharField(max_length=45)),
                ('version', models.CharField(max_length=64)),
                ('db_filename', models.CharField(max_length=256)),
                ('ps_filename', models.CharField(max_length=256)),
                ('hs_filename', models.CharField(max_length=256)),
                ('date', models.DateTimeField()),
                ('user', models.CharField(max_length=45)),
                ('ciwp', models.ForeignKey(to='deployment.CIWP')),
                ('db_list', models.ManyToManyField(to='deployment.DataBin')),
                ('hs_free_list', models.ManyToManyField(related_name='hs_free_list', to='deployment.ProcessServer')),
                ('hs_list', models.ManyToManyField(related_name='hs_list', to='deployment.ProcessServer')),
                ('panel', models.ForeignKey(to='detection.Panel')),
                ('ps_list', models.ManyToManyField(related_name='ps_list', to='deployment.ProcessServer')),
            ],
            options={
                'ordering': ['-id', '-date'],
            },
        ),
    ]

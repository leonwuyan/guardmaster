# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('operating', '0008_auto_20150630_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='ssh_port',
            field=models.IntegerField(default=22, help_text='SSH Port, Usually Is 22'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='server',
            name='port',
            field=models.IntegerField(help_text='GM Port, Usually Is 9135'),
        ),
    ]

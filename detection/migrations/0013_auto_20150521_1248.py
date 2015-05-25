# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0012_auto_20150505_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uicolmap',
            name='col_type',
            field=models.CharField(blank=True, max_length=45, null=True, choices=[(b'timestamp_to_time', 'timestamp to time'), (b'channel_list', 'channel list'), (b'identity_str', 'anything to string'), (b'ratio_two', 'ratio two'), (b'zone_list', 'zone list'), (b'time', 'time'), (b'float_two', 'float two'), (b'timestamp_to_date', 'timestamp to date'), (b'date', 'date')]),
        ),
        migrations.AlterField(
            model_name='uisubmenu',
            name='category',
            field=models.CharField(blank=True, max_length=45, null=True, help_text='Category is required when Main menu is selected', choices=[(b'operating:mail', 'mail'), (b'detection:deal_query', 'deal_query'), (b'detection:count', 'count'), (b'operating:single', 'single'), (b'detection:user_query', 'user_query'), (b'operating:notify', 'notify'), (b'detection:gang_query', 'gang_query')]),
        ),
        migrations.AlterField(
            model_name='uisubmenu',
            name='url',
            field=models.CharField(max_length=200, db_index=True),
        ),
    ]

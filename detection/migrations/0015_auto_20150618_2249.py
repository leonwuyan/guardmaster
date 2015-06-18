# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0014_auto_20150610_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='panel',
            name='symbol',
            field=models.CharField(default='cymsl', max_length=45),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uicolmap',
            name='col_type',
            field=models.CharField(blank=True, max_length=45, null=True, choices=[(b'timestamp_to_time', 'timestamp to time'), (b'channel_list', 'channel list'), (b'identity_str', 'anything to string'), (b'ratio_two', 'ratio two'), (b'zone_list', 'zone list'), (b'date', 'date'), (b'time', 'time'), (b'contact_reply', 'contact to reply'), (b'float_two', 'float two'), (b'timestamp_to_date', 'timestamp to date'), (b'ip_to_server', 'ip to server')]),
        ),
        migrations.AlterField(
            model_name='uisubmenu',
            name='category',
            field=models.CharField(blank=True, max_length=45, null=True, help_text='Category is required when Main menu is selected', choices=[(b'detection:count_without_time', 'count_without_time'), (b'operating:contact', 'contact'), (b'detection:deal_query', 'deal_query'), (b'operating:mail', 'mail'), (b'detection:count', 'count'), (b'operating:single', 'single'), (b'detection:user_query', 'user_query'), (b'detection:history_query', 'history_query'), (b'operating:notify', 'notify'), (b'operating:rank', 'rank'), (b'detection:count_only_time', 'count_only_time'), (b'detection:gang_query', 'gang_query')]),
        ),
    ]

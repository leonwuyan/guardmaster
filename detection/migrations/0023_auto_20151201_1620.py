# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0022_auto_20151104_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='panel',
            name='db_aliases',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='uicolmap',
            name='col_type',
            field=models.CharField(blank=True, max_length=45, null=True, choices=[(b'timestamp_to_time', 'timestamp to time'), (b'channel_list', 'channel list'), (b'identity_str', 'anything to string'), (b'ratio_two', 'ratio two'), (b'zone_list', 'zone list'), (b'date', 'date'), (b'time', 'time'), (b'contact_reply', 'contact to reply'), (b'user_status_list', 'user status list'), (b'float_two', 'float two'), (b'kick_ban', 'kick ban user'), (b'pay_channel_list', 'pay channel list'), (b'ip_to_server', 'ip to server'), (b'timestamp_to_date', 'timestamp to date'), (b'chat_type_list', 'chat type list')]),
        ),
        migrations.AlterField(
            model_name='uisubmenu',
            name='category',
            field=models.CharField(blank=True, max_length=45, null=True, help_text='Category is required when Main menu is selected', choices=[(b'detection:count_without_time', 'count_without_time'), (b'operating:contact', 'contact'), (b'detection:everyday_deal_query', 'everyday_deal_query'), (b'detection:everyday_history_query', 'everyday_history_query'), (b'detection:deal_query', 'deal_query'), (b'operating:mail', 'mail'), (b'detection:count', 'count'), (b'operating:single', 'single'), (b'detection:count_with_pay_channel', 'count_with_pay_channel'), (b'detection:user_query', 'user_query'), (b'deployment:control', 'control'), (b'operating:notify', 'notify'), (b'deployment:patch', 'patch'), (b'operating:rank', 'rank'), (b'deployment:config', 'config'), (b'detection:history_query', 'history_query'), (b'detection:count_only_time', 'count_only_time'), (b'detection:chat_query', 'chat_query'), (b'operating:all_mail', 'all_mail'), (b'detection:gang_query', 'gang_query')]),
        ),
    ]

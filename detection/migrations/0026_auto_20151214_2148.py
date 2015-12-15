# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0025_uisubmenu_is_bak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uisubmenu',
            name='category',
            field=models.CharField(blank=True, max_length=45, null=True, help_text='Category is required when Main menu is selected', choices=[(b'detection:everyday_deal_query', 'everyday_deal_query'), (b'operating:mail', 'mail'), (b'operating:notify', 'notify'), (b'detection:everyday_history_query', 'everyday_history_query'), (b'detection:deal_query', 'deal_query'), (b'detection:ban_query', 'ban_query'), (b'deployment:control', 'control'), (b'detection:online', 'online'), (b'detection:count_without_time', 'count_without_time'), (b'operating:contact', 'contact'), (b'operating:all_mail', 'all_mail'), (b'operating:single', 'single'), (b'deployment:patch', 'patch'), (b'operating:rank', 'rank'), (b'detection:gang_query', 'gang_query'), (b'detection:count_with_pay_channel', 'count_with_pay_channel'), (b'detection:chat_query', 'chat_query'), (b'detection:user_query', 'user_query'), (b'deployment:pre_update', 'pre_update'), (b'detection:count', 'count'), (b'deployment:config', 'config'), (b'detection:history_query', 'history_query'), (b'detection:count_only_time', 'count_only_time')]),
        ),
    ]

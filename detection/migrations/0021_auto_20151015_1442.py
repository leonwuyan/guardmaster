# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0020_auto_20151014_1103'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uisubmenu',
            name='category',
            field=models.CharField(blank=True, max_length=45, null=True, help_text='Category is required when Main menu is selected', choices=[(b'detection:count_without_time', 'count_without_time'), (b'operating:contact', 'contact'), (b'detection:everyday_deal_query', 'everyday_deal_query'), (b'detection:everyday_history_query', 'everyday_history_query'), (b'detection:deal_query', 'deal_query'), (b'operating:mail', 'mail'), (b'deployment:config', 'config'), (b'operating:single', 'single'), (b'detection:count_with_pay_channel', 'count_with_pay_channel'), (b'detection:user_query', 'user_query'), (b'operating:notify', 'notify'), (b'deployment:patch', 'patch'), (b'operating:rank', 'rank'), (b'detection:count', 'count'), (b'deployment:control', 'control'), (b'detection:history_query', 'history_query'), (b'detection:count_only_time', 'count_only_time'), (b'detection:gang_query', 'gang_query')]),
        ),
    ]

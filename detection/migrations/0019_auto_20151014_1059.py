# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detection', '0018_auto_20150907_2005'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uimainmenu',
            options={'ordering': ['group', 'seqid']},
        ),
        migrations.AddField(
            model_name='panel',
            name='start_time',
            field=models.DateField(default='2015-6-27'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='uisubmenu',
            name='category',
            field=models.CharField(blank=True, max_length=45, null=True, help_text='Category is required when Main menu is selected', choices=[(b'detection:count_without_time', 'count_without_time'), (b'operating:contact', 'contact'), (b'detection:everyday_deal_query', 'everyday_deal_query'), (b'detection:everyday_history_query', 'everyday_history_query'), (b'detection:deal_query', 'deal_query'), (b'operating:mail', 'mail'), (b'deployment:config', 'config'), (b'operating:single', 'single'), (b'detection:count_with_pay_channel', 'count_with_pay_channel'), (b'detection:user_query', 'user_query'), (b'operating:notify', 'notify'), (b'deployment:patch', 'patch'), (b'operating:rank', 'rank'), (b'detection:count', 'count'), (b'detection:history_query', 'history_query'), (b'detection:count_only_time', 'count_only_time'), (b'detection:gang_query', 'gang_query')]),
        ),
    ]

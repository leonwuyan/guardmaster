# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('detection', '0015_auto_20150618_2249'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='uimainmenu',
            name='groups',
        ),
        migrations.AddField(
            model_name='uimainmenu',
            name='group',
            field=models.ForeignKey(default=1, to='auth.Group'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='uimainmenu',
            name='panels',
            field=models.ManyToManyField(to='detection.Panel'),
        ),
        migrations.AlterField(
            model_name='uicolmap',
            name='col_type',
            field=models.CharField(blank=True, max_length=45, null=True, choices=[(b'timestamp_to_time', 'timestamp to time'), (b'channel_list', 'channel list'), (b'identity_str', 'anything to string'), (b'ratio_two', 'ratio two'), (b'zone_list', 'zone list'), (b'time', 'time'), (b'contact_reply', 'contact to reply'), (b'float_two', 'float two'), (b'ip_to_server', 'ip to server'), (b'timestamp_to_date', 'timestamp to date'), (b'date', 'date')]),
        ),
        migrations.AlterField(
            model_name='uisubmenu',
            name='category',
            field=models.CharField(blank=True, max_length=45, null=True, help_text='Category is required when Main menu is selected', choices=[(b'detection:count_without_time', 'count_without_time'), (b'operating:contact', 'contact'), (b'detection:deal_query', 'deal_query'), (b'operating:mail', 'mail'), (b'detection:count', 'count'), (b'operating:single', 'single'), (b'detection:user_query', 'user_query'), (b'operating:notify', 'notify'), (b'operating:rank', 'rank'), (b'detection:history_query', 'history_query'), (b'detection:count_only_time', 'count_only_time'), (b'detection:gang_query', 'gang_query')]),
        ),
    ]

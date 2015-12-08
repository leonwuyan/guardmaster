from django.conf.urls import url
from . import views, auth_views

urlpatterns = [
    url(
        r'^(?P<panel_id>[0-9]+)/user_query/(?P<url>[_A-Za-z]+)$',
        views.user_query,
        name='user_query'),
    url(
        r'^(?P<panel_id>[0-9]+)/gang_query/(?P<url>[_A-Za-z]+)$',
        views.gang_query,
        name='gang_query'),
    url(
        r'^(?P<panel_id>[0-9]+)/deal_query/(?P<url>[_A-Za-z]+)$',
        views.deal_query,
        name='deal_query'),
    url(
        r'^(?P<panel_id>[0-9]+)/everyday_deal_query/(?P<url>[_A-Za-z]+)$',
        views.everyday_deal_query,
        name='everyday_deal_query'),
    url(
        r'^(?P<panel_id>[0-9]+)/history_query/(?P<url>[_A-Za-z]+)$',
        views.history_query,
        name='history_query'),
    url(
        r'^(?P<panel_id>[0-9]+)/everyday_history_query/(?P<url>[_A-Za-z]+)$',
        views.everyday_history_query,
        name='everyday_history_query'),
    url(
        r'^(?P<panel_id>[0-9]+)/chat_query/(?P<url>[_A-Za-z]+)$',
        views.chat_query,
        name='chat_query'),
    url(
        r'^(?P<panel_id>[0-9]+)/(?P<t_p>[_A-Za-z]+)/(?P<url>[_A-Za-z]+).json$',
        views.json_template,
        name='json_template'),
    url(
        r'^(?P<panel_id>[0-9]+)/count/(?P<url>[_A-Za-z]+)$',
        views.count,
        name='count'),
    url(
        r'^(?P<panel_id>[0-9]+)/count_with_pay_channel/(?P<url>[_A-Za-z]+)$',
        views.count_with_pay_channel,
        name='count_with_pay_channel'),
    url(
        r'^(?P<panel_id>[0-9]+)/count_without_time/(?P<url>[_A-Za-z]+)$',
        views.count_without_time,
        name='count_without_time'),
    url(
        r'^(?P<panel_id>[0-9]+)/count_only_time/(?P<url>[_A-Za-z]+)$',
        views.count_only_time,
        name='count_only_time'),
    url(
        r'^(?P<panel_id>[0-9]+)/online/(?P<url>[_A-Za-z]+)$',
        views.online,
        name='online'),
    url(r'^$', auth_views.index, name='default_index'),
]

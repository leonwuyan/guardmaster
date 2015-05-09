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
        r'^(?P<panel_id>[0-9]+)/(?P<t_p>[_A-Za-z]+)/(?P<url>[_A-Za-z]+).json$',
        views.json_template,
        name='json_template'),
    url(
        r'^(?P<panel_id>[0-9]+)/count/(?P<url>[_A-Za-z]+)$',
        views.count,
        name='count'),
    url(r'^$', auth_views.index, name='default_index'),
]

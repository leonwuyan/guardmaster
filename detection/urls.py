from django.conf.urls import url
from . import views, auth_views

urlpatterns = [
    url(
        r'^(?P<panel_id>[0-9]+)/query/(?P<url>[A-Za-z]+)$',
        views.query,
        name='query'),
    url(
        r'^(?P<panel_id>[0-9]+)/query/(?P<url>[A-Za-z]+).json$',
        views.query_json,
        name='query_json'),
    url(
        r'^(?P<panel_id>[0-9]+)/count/(?P<url>[A-Za-z]+).json$',
        views.count_json,
        name='count_json'),
    url(
        r'^(?P<panel_id>[0-9]+)/count/(?P<url>[A-Za-z]+)$',
        views.count,
        name='count'),
    url(r'^$', auth_views.index, name='default_index'),
]

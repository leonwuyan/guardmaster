from django.conf.urls import patterns, include, url
from deployment import views

urlpatterns = [
    url(
        r'^(?P<panel_id>[0-9]+)/config/(?P<url>[_A-Za-z]+)/$',
        views.config,
        name='config'),
    url(
        r'^(?P<panel_id>[0-9]+)/patch/(?P<url>[_A-Za-z]+)/$',
        views.patch,
        name='patch'),
    url(
        r'^(?P<panel_id>[0-9]+)/control/(?P<url>[_A-Za-z]+)/$',
        views.control,
        name='control'),
    url(
        r'^(?P<panel_id>[0-9]+)/(?P<hostname_id>[0-9]+)/(?P<platform>[a-z]+)/(?P<channel>[0-9]+)/(?P<version>[a-zA-Z]+).json$',
        views.version,
        name='version'),
    url(
        r'^(?P<panel_id>[0-9]+)/pre_update/(?P<url>[_A-Za-z]+)/$',
        views.pre_update,
        name='pre_update'),
]

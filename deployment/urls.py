from django.conf.urls import patterns, include, url
from deployment import views

urlpatterns = [
    url(
        r'^(?P<panel_id>[0-9]+)/config/(?P<url>[_A-Za-z]+)/$',
        views.config,
        name='config'),
    url(
        r'^(?P<panel_id>[0-9]+)/config/(?P<url>[_A-Za-z]+)/(?P<tpltemplate_id>[0-9]+)/$',
        views.config,
        name='config_tpl'),
    url(
        r'^(?P<panel_id>[0-9]+)/patch/(?P<url>[_A-Za-z]+)/$',
        views.patch,
        name='patch'),
    url(
        r'^(?P<panel_id>[0-9]+)/(?P<hostname_id>[0-9]+)/(?P<platform>[a-z]+)/(?P<channel>[0-9]+)/(?P<version>[a-zA-Z]+).json$',
        views.version,
        name='version'),
]

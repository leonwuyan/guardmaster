from django.conf.urls import patterns, include, url
from deployment import views

urlpatterns = [
    url(
        r'^(?P<panel_id>[0-9]+)/patch/(?P<url>[_A-Za-z]+)$',
        views.patch,
        name='patch'),
    url(
        r'^(?P<panel_id>[0-9]+)/(?P<hostname_id>[0-9]+)/(?P<platform>[a-z]+)/(?P<channel>[0-9]+)/version.json$',
        views.version,
        name='version'),
]

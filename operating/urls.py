from django.conf.urls import url
from . import views as operating_views
from detection import auth_views, views

urlpatterns = [
    url(
        r'^(?P<panel_id>[0-9]+)/(?P<t_p>[_A-Za-z]+)/(?P<url>[_A-Za-z]+).json$',
        views.json_template,
        name='json_template'),
    url(
        r'^(?P<panel_id>[0-9]+)/notify/(?P<url>[_A-Za-z]+)$',
        operating_views.notify,
        name='notify'),
    url(
        r'^(?P<panel_id>[0-9]+)/mail/(?P<url>[_A-Za-z]+)$',
        operating_views.mail,
        name='mail'),
    url(r'^$', auth_views.index, name='default_index'),
]

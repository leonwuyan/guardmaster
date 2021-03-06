from django.conf.urls import url
from . import views
from detection import auth_views
from detection import views as detection_views

urlpatterns = [
    url(
        r'^(?P<panel_id>[0-9]+)/(?P<t_p>[_A-Za-z]+)/(?P<url>[_A-Za-z]+).json$',
        detection_views.json_template,
        name='json_template'),
    url(
        r'^(?P<panel_id>[0-9]+)/notify/(?P<url>[_A-Za-z]+)$',
        views.notify,
        name='notify'),
    url(
        r'^(?P<panel_id>[0-9]+)/notify/(?P<id>[0-9]+)$',
        views.edit_notify,
        name='edit_notify'),
    url(
        r'^(?P<panel_id>[0-9]+)/mail/(?P<url>[_A-Za-z]+)$',
        views.mail,
        name='mail'),
    url(
        r'^(?P<panel_id>[0-9]+)/all_mail/(?P<url>[_A-Za-z]+)$',
        views.all_mail,
        name='all_mail'),
    url(
        r'^(?P<panel_id>[0-9]+)/rank/(?P<url>[_A-Za-z]+)$',
        views.rank,
        name='rank'),
    url(
        r'^(?P<panel_id>[0-9]+)/single/(?P<url>[_A-Za-z]+)$',
        views.single,
        name='single'),
    url(
        r'^(?P<panel_id>[0-9]+)/single/(?P<url>[_A-Za-z]+)/(?P<type>[_0-9a-zA-Z]+).json$',
        views.change_single,
        name='change_single'),
    url(
        r'^(?P<panel_id>[0-9]+)/contact/(?P<url>[_A-Za-z]+)$',
        views.contact,
        name='contact'),
    url(
        r'^(?P<panel_id>[0-9]+)/contact/(?P<issue_id>[0-9]+)$',
        views.contact_reply,
        name='contact_reply'),
    url(
        r'^(?P<panel_id>[0-9]+)/contact/(?P<issue_id>[0-9]+).json$',
        views.contact_status,
        name='contact_status'),
    url(
        r'^(?P<panel_id>[0-9]+)/guard_master_order/(?P<url>[_A-Za-z]+)$',
        views.guard_master_order,
        name='guard_master_order'),
    url(r'^$', auth_views.index, name='default_index'),
]

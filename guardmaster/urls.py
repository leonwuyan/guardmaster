from django.views.i18n import javascript_catalog
from django.conf.urls import include, url
from django.contrib import admin
from detection import auth_views
js_info_dict = {
    'packages': ('detection',),
}
urlpatterns = [
    # Examples:
    # url(r'^$', 'guardmaster.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^jsi18n/$', javascript_catalog, js_info_dict),
    url(r'^polls/', include('polls.urls', namespace="polls")),
    url(r'^detection/', include('detection.urls', namespace='detection')),
    url(r'^operating/', include('operating.urls', namespace='operating')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', auth_views.index, name='index'),
    url(r'^login/$', auth_views.user_login, name='user_login'),
    url(r'^logout/$', auth_views.user_logout, name='user_logout'),
]

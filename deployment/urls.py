from django.conf.urls import patterns, include, url
from deployment.views import Hello

urlpatterns = [
    url(r'^$', Hello.as_view()),
]

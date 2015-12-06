__author__ = 'diwakarmahajan'
from django.conf.urls import url
from poll import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^poll/$', views.poll_list),
    url(r'^poll/(?P<pk>[0-9]+)/$', views.poll_detail),
]

urlpatterns = format_suffix_patterns(urlpatterns)
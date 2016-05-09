from django.conf.urls.defaults import *
from store import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'/(?P<pk>[\d]+)/$', views.page_item),
    url(r'^(?P<slug>[\w\-]+)/$', views.category),
    url(r'^[\w\-]+/(?P<slug>[\w\-]+)/$', views.category),
    url(r'^[\w\-]+/[\w\-]+/(?P<slug>[\w\-]+)/$', views.category),
)


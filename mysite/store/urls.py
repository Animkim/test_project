from django.conf.urls.defaults import *
from store import views

urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^(?P<category_name>[\w\-]+)/$', views.category),
    url(r'^[\w\-]+/(?P<category_name>[\w\-]+)/$', views.category),
    url(r'^[\w\-]+/[\w\-]+/(?P<category_name>[\w\-]+)/$', views.category),
    url(r'^/search/$', views.search),

)

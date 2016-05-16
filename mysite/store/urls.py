from django.conf.urls.defaults import *
from store import views


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'product/([\w\-]+)', views.product_page),
    url(r'^([\w\D\-]+)/$', views.category),
    )


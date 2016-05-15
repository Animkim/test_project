from django.conf.urls.defaults import *
from store import views


urlpatterns = patterns('',
    url(r'^$', views.index),
    url(r'^search/$', views.search),
    url(r'([\D\-]+)/$', views.category),
    url(r'[\w\-]+/(?P<slug>[\w\-]+)/$', views.product_page),
<<<<<<< HEAD
=======

>>>>>>> 8c1882331db924f0e42170ba518de5ee70c1708b
)


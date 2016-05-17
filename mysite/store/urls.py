from django.conf.urls.defaults import *


urlpatterns = patterns('store.views',
    url(r'^$', 'index'),
    url(r'^search/$', 'search'),
    url(r'product/([\w\-]+)', 'product_page'),
    url(r'^([\w\D\-]+)/$', 'category'),
    )


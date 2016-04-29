from django.conf.urls.defaults import *
from mysite.store.views import index

urlpatterns = patterns('',
    url(r'^$', index),
)

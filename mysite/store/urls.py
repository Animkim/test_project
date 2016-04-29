from django.conf.urls.defaults import *
from mysite.store.views import category

urlpatterns = patterns('',
    url(r'^$', category),
)

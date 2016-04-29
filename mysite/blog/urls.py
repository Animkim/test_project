from django.conf.urls.defaults import *
from blog import views

urlpatterns = patterns('',
    url(r'^$', views.archive),
)

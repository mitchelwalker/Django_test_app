from django.conf.urls import patterns, url
import re
from testsite import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
)

from django.conf.urls import patterns, url
import re
from homepage import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home'),
)


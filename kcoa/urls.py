from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
	url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'kcoa.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^$', 'joins.views.home', name ='home'),
    url(r'^(?P<ref_id>.*)$', 'joins.views.share', name ='share'),
]

from django.conf.urls import patterns, include, url
from django.contrib import admin
from albums.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'music.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^$', index, name='index'),
	url(r'^stream/(?P<t>\w+)/$', stream, name="stream")
)

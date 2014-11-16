from django.conf.urls import patterns, include, url
from django.contrib import admin
from albums.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^album/(?P<album_slug>[\w-]+)/$', album, name="album"),
	url(r'^stream/(?P<t>\w+)/$', stream, name="stream"),
	url(r'^$', index, name='index')
)

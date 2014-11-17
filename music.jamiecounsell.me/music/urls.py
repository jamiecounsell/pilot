from django.conf.urls import patterns, include, url
from django.contrib import admin
from albums.views import *
from users.views import *

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
	url(r'^album/(?P<album_slug>[\w-]+)/$', album, name="album"),
	url(r'^stream/(?P<t>\w+)/$', stream, name="stream"),
	url(r'^charge/', charge, name="charge"),
	url(r'^download/(?P<t>[\w-]+)/$', download, name="download"),
	url(r'^$', index, name='index')
)

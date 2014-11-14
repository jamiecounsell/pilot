from django.contrib import admin
from albums.models import Album, Track

class TrackInline(admin.TabularInline):
	model = Track
	min_num = 1

class AlbumAdmin(admin.ModelAdmin):
	inlines = [TrackInline]

admin.site.register(Album, AlbumAdmin)
admin.site.register(Track)
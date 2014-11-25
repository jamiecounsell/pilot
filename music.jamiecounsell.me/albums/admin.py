from django.contrib import admin
from albums.models import Album, Track, TrackToken, BonusContent

class TrackInline(admin.TabularInline):
	model = Track
	fields = [
			'track_number',
			'name',
			'lyrics',
		]
	min_num = 1

class BonusInline(admin.TabularInline):
	model = BonusContent
	min_num = 1

class AlbumAdmin(admin.ModelAdmin):
	inlines = [TrackInline, BonusInline]
	def get_readonly_fields(self, request, obj=None):
		actions_on_top = False
		if not obj:
			return ['add_date',
					'slug']
		else:
			return ['add_date',
					'slug']



admin.site.register(Album, AlbumAdmin)
admin.site.register(TrackToken)
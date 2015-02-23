from django.contrib import admin
from albums.models import Album, Track, TrackToken, BonusContent

class TrackInline(admin.TabularInline):
	model = Track
	fields = [
			'track_number',
			'name',
			'lyrics',
			'audio_file'
		]
	min_num = 1

class BonusInline(admin.TabularInline):
	model = BonusContent
	min_num = 0

class AlbumAdmin(admin.ModelAdmin):
	inlines = [TrackInline, BonusInline]
	def get_readonly_fields(self, request, obj=None):
		actions_on_top = False
		common = [	'add_date',
					'slug',
					'zipfile'
				 ]
		if not obj:
			return common + []
		else:
			return common + []
	def response_add(self, request, new_object):
		obj = self.post_inline_save(new_object)
		return super(AlbumAdmin, self).response_add(request, obj)

	def response_change(self, request, obj):
		obj = self.post_inline_save(obj)
		return super(AlbumAdmin, self).response_change(request, obj)

	def post_inline_save(self, obj):
		obj.createZipFile()
		return obj

admin.site.register(Album, AlbumAdmin)
admin.site.register(TrackToken)
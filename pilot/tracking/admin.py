from django.contrib import admin
from tracking.models import SongTrackingMilestone, SongTrackingRecord

# Register your models here.

class SongTrackingMilestoneAdmin(admin.ModelAdmin):

	fields = (
		'name',
		'mark',
	)

class SongTrackingRecordAdmin(admin.ModelAdmin):
	readonly_fields = (
		'created',
		'updated'
	)

	fields = (
		'created',
		'updated',
		'milestone'
	)

admin.site.register(SongTrackingMilestone, SongTrackingMilestoneAdmin)
admin.site.register(SongTrackingRecord, SongTrackingRecordAdmin)
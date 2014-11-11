from django.contrib import admin
from users.models import Purchase

class PurchaseAdmin(admin.ModelAdmin):

	def get_readonly_fields(self, request, obj=None):
		if obj:
			return [
				'download_link',
				'download_pin',
				'album',
				'user'
			]
		else:
			return []

admin.site.register(Purchase, PurchaseAdmin)
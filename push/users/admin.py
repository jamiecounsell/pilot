from django.contrib import admin
from users.models import Purchase

def resend_emails(self, request, queryset):
	for q in queryset:
		q.send_email()

resend_emails.short_description="Resend Purchase Email"

class PurchaseAdmin(admin.ModelAdmin):

	actions = [resend_emails]

	def get_readonly_fields(self, request, obj=None):
		if obj:
			return [
				'download_token',
				'download_pin',
				'album',
				'email'
			]
		else:
			return []

admin.site.register(Purchase, PurchaseAdmin)
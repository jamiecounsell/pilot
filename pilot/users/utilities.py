from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import Context
from django.conf import settings
from django.db.models.query import EmptyQuerySet
from albums.models import Track, BonusContent
from albums.utilities import trackSort
from django.http import HttpResponse, Http404

import zipfile, StringIO, os

def sendPurchaseEmail(template, context, purchase):
	subject	  = "Your " + purchase.album.name + " Digital Download Purchase"
	from_email, to = settings.DEFAULT_FROM_EMAIL, purchase.email

	text_content = render_to_string('email_purchase.txt', context)
	html_content = render_to_string('email_purchase.html', context)

	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def generateZipResponse(z, album):
	z_path = os.path.join(settings.MEDIA_URL, os.path.relpath(z.path, settings.MEDIA_ROOT))
	response = HttpResponse()

	response['Content-Disposition'] = 'attachment; filename=%s' % (album.name)
	response['Content-Type'] = 'application/octet-stream'
	response['X-Accel-Redirect'] = '%s' % (z_path, )	
	return response

def zipForDownload(album):

	try:
		z = album.zipfile
		if not z:
			raise Exception
		response = generateZipResponse(z, album)
	# Fallback if there is no file. TODO clean this up or reuse this function
	# since the (almost) same function is used in albums.models:Album
	except Exception:
		album.save()
		z = album.zipfile
		if not z:
			raise Exception
		generateZipResponse(z, album)	
	return response




from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import Context
from django.conf import settings
from albums.models import Track
import zipfile, StringIO

def sendPurchaseEmail(template, context, purchase):
	subject	  = "Your " + purchase.album.name + " Digital Download Purchase"
	from_email, to = settings.DEFAULT_FROM_EMAIL, purchase.email

	print context['album'].background.url

	text_content = render_to_string('email_purchase.txt', context)
	html_content = render_to_string('email_purchase.html', context)

	msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
	msg.attach_alternative(html_content, "text/html")
	msg.send()

def zipForDownload(album):

	tracks = Track.objects.filter(album=album)
	zipped_file = StringIO.StringIO()
	with zipfile.ZipFile(zipped_file, 'w') as zip:
		for i, f in tracks:
			print i, f
			f.seek(0)
			zip.writestr("{}".format(i), f.read())




from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.template import Context
from django.conf import settings
from albums.models import Track
from django.http import HttpResponse
import zipfile, StringIO, os

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
	track_files = [open(f.audio_file.path, 'rb') for f in tracks]
	zipped_file = StringIO.StringIO()
	with zipfile.ZipFile(zipped_file, 'w') as zip:
		for i, f in enumerate(track_files):
			f.seek(0)
			name = tracks[i].name
			ext = os.path.basename(f.name).split('.')[-1]
			zip.writestr("{0}.{1}".format(name, ext), f.read())

	zipped_file.seek(0)
	response = HttpResponse(zipped_file, content_type='application/octet-stream')
	response['Content-Disposition'] = 'attachment; filename=%s.zip' % (album.name)
	return response




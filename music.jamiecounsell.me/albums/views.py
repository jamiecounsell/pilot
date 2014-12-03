from albums.models import Album, Track, TrackToken
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseForbidden, Http404
from albums.utilities import FileIterWrapper
from django.conf import settings
from django.template import RequestContext
from users.models import Purchase
from albums.utilities import trackSort
import os, datetime, calendar, time, json

def stream(request, t):
	try:
		token = request.GET.get('tracktoken')
		token = TrackToken.objects.get(token=token)
		if abs(calendar.timegm(time.gmtime()) - token.date) > 10:
			token.delete()
			raise TrackToken.DoesNotExist
		elif token.counter >= 3:
			token.delete()
			raise TrackToken.DoesNotExist
		elif not request.mobile:
			token.delete()
		else:
			token.counter = token.counter + 1
			token.save()

		if not token:
			raise KeyError
	except (KeyError, TrackToken.DoesNotExist) as e:
		return HttpResponseForbidden()

	try:
		track = Track.objects.get(pk=t)
	except Track.DoesNotExist:
		raise Http404

	response = HttpResponse()
	response['Content-Type'] = 'audio/mp3'
	response['Content-Disposition'] = 'attachment; filename=%s' % (track.audio_file, )
	response['X-Accel-Redirect'] = '%s' % (track.audio_file.url, )
	
	return response

def index(request):
	try:
		a = Album.objects.get(featured=True, hidden=False)
		if not a:
			raise Exception
	except Exception:
		a = Album.objects.all().order_by('-id')[0]

	return album(request, a.slug)

def album(request, album_slug):
	album = Album.objects.get(slug=album_slug)
	if not album:
		album = Album.objects.all().order_by('-id')[0]
	tracks = trackSort(list(Track.objects.filter(album=album)))
	tokens = {}
	for t in tracks:
			tok = TrackToken(track=t, date=calendar.timegm(time.gmtime()), counter=0)
			tok.save()
			tokens[t] = tok

	context =  {"album":album, 
				"albums":Album.objects.filter(hidden=False),
				"tracks":tracks, 
				"tokens":tokens,
				"stripe_key":settings.STRIPE_PUBLISHABLE_KEY,
				"ABS_URL":settings.SITE_URL + "album/%s" % (album.slug)}

	return render_to_response('album.html', context, context_instance=RequestContext(request))


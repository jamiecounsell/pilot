from django.shortcuts import render
from albums.models import Album, Track, TrackToken
from django.shortcuts import render, render_to_response
from django.http import HttpResponse, HttpResponseForbidden, Http404
from albums.utilities import FileIterWrapper
import os, datetime

def stream(request, t):
	try:
		token = request.GET.get('tracktoken')
		token = TrackToken.objects.get(token=token)
		token.delete()
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
	request_album = Album.objects.get(featured=True)
	try:
		a = Album.objects.get(featured=True)
	except Exception:
		a = Album.objects.all().order_by('-id')[0]

	return album(request, a.pk)

def album(request, album):
	request_album = Album.objects.get(featured=True)
	album = Album.objects.get(featured=True)
	if not album:
		album = Album.objects.all().order_by('-id')[0]
	tracks = Track.objects.filter(album=album)
	tokens = {}
	for t in tracks:
			tok = TrackToken(track=t, date=datetime.datetime.now())
			tok.save()
			tokens[t] = tok

	context = {"album":album, "tracks":tracks, "tokens":tokens}
	return render_to_response('album.html', context)

def charge(request):
	pass
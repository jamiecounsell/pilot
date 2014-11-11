from django.shortcuts import render
from albums.models import Album
from django.shortcuts import render, render_to_response

def index(request):
	request_album = Album.objects.get(featured=True)
	context = {}
	return render_to_response('album.html', context)
def album(request):
	pass

def charge(request):
	pass
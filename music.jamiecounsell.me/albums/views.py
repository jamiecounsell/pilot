from django.shortcuts import render
from albums.models import Album, Track
from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import os

class FileIterWrapper(object):
	def __init__(self, flo, chunk_size = 1024**2):
		self.flo = flo
		self.chunk_size = chunk_size

	def next(self):
		data = self.flo.read(self.chunk_size)
		if data:
			return data
		else:
			raise StopIteration

	def __iter__(self):
		return self

def index(request):
	request_album = Album.objects.get(featured=True)
	album = Album.objects.all()[0]
	print album
	tracks = Track.objects.filter(album=album)
	context = {"album":album, "tracks":tracks}
	return render_to_response('album.html', context)

def album(request):
	pass

def charge(request):
	pass
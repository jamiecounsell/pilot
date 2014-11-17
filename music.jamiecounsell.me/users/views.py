from django.shortcuts import render, render_to_response
from users.models import Purchase
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.template import RequestContext


def download(request, t):

	try:
		purchase = Purchase.objects.get(download_token=t)
	except Purchase.DoesNotExist:
		raise Http404

	if request.method == "GET":
		return downloadPrePin(request, purchase)
	elif request.method == "POST":
		return downloadPostPin(request, purchase)
	else:
		return HttpResponseForbidden()

def downloadPrePin(request, purchase):
	from_site = False
	try:
		if 'music.jamiecounsell.me' in request.META['HTTP_REFERER'].split('/')\
		or 'music.jamiecounsell.com' in request.META['HTTP_REFERER'].split('/'):
			from_site = True
	except KeyError:
		pass

	context = {'from_site':from_site, 'album':purchase.album, 'user_email':purchase.email}
	
	return render_to_response('purchase.html', context, context_instance=RequestContext(request))

def downloadPostPin(request, purchase):
	if request.POST.get('PIN').encode('utf-8') == purchase.download_pin.encode('utf-8'):
		for track in Track.objects.filter(album=purchase.album):
			pass
	else:
		return HttpResponseForbidden()
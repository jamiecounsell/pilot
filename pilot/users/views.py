from django.shortcuts import render, render_to_response
from albums.models import Album
from users.models import Purchase
from django.http import HttpResponse, HttpResponseForbidden, Http404
from django.template import RequestContext
from users.utilities import sendPurchaseEmail
from django.conf import settings
from users.utilities import zipForDownload
import stripe, json

stripe.api_key = settings.STRIPE_SECRET_KEY

def charge(request):
	stoken = request.POST.get('stoken')
	email = request.POST.get('email')
	album_id = request.POST.get('album')

	try:
		album = Album.objects.get(id=album_id)
	except Album.DoesNotExist:
		album = None

	if request.method == "GET":
		return HttpResponseForbidden()

	elif not stoken or not email or not album:
		raise Http404
	else:
		#We have a token, email, and album in a POST request
		new_purchase = Purchase(album=album, email=email)

		amount = int(album.price_incents)

		customer = stripe.Customer.create(
			email=email,
			card=stoken
		)
		charge = stripe.Charge.create(
			customer=customer.id,
			amount=amount,
			currency='cad',
			description=album.name + " digital download."
		)

		new_purchase.save()

		response_data = {}

		response_data["redirecturl"] = settings.SITE_URL + "download/" + new_purchase.download_token
		return HttpResponse(json.dumps(response_data), content_type="application/json")

def download(request, t):
	try:
		purchase = Purchase.objects.get(download_token=t)
	except Purchase.DoesNotExist:
		raise Http404

	if request.method == "GET":
		return downloadPrePin(request, purchase, None)
	elif request.method == "POST":
		return downloadPostPin(request, purchase)
	else:
		return HttpResponseForbidden()

def downloadPrePin(request, purchase, error):
	from_site = False
	try:
		# Determine if this is a redirect from the site or a click from an email
		# This doesn't need to be reliable, it's just for aesthetics on the front-end
		if 'music.jamiecounsell.me' in request.META['HTTP_REFERER'].split('/')\
		or 'music.jamiecounsell.com' in request.META['HTTP_REFERER'].split('/'):
			from_site = True
	except KeyError:
		pass

	# Get URL to point the PIN POST request at
	URL = request.get_full_path
	context = {'from_site':from_site, 'album':purchase.album, 'user_email':purchase.email, 'url':URL, "error":error}
	
	return render_to_response('purchase.html', context, context_instance=RequestContext(request))

def downloadPostPin(request, purchase):
	if request.POST.get('PIN').encode('utf-8') == purchase.download_pin.encode('utf-8'):
		# Get zip response with all tracks and bonus content
		resp = zipForDownload(purchase.album)
		return resp

	else:
		# Otherwise, return the same page again with an error
		error = "Invalid PIN. Please try again!"
		return downloadPrePin(request, purchase, error)
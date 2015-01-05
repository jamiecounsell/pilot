from django.db import models
from django.conf import settings
from albums.models import Album
from users.utilities import sendPurchaseEmail
import hashlib, random, time, calendar


class Purchase(models.Model):
	email = models.CharField(max_length=100, null=True, blank=True, verbose_name="User Email")
	album = models.ForeignKey(Album)
	time = models.DateTimeField(auto_now=True, auto_now_add=True)

	download_token = models.CharField(max_length=500, blank=True, null=True)
	download_pin = models.CharField(max_length=10, blank=True, null=True)

	def stripe_charge(self):
		pass

	def generate_link(self):
		# Hash user email and date purchased to create unique link
		user_email = str(self.email)
		date_purchased = str(self.time)
		hashed = hashlib.sha256((user_email + date_purchased + str(calendar.timegm(time.gmtime()))).encode('utf-8')).hexdigest()
		self.download_token = hashed

	def generate_pin(self):
		# Generate random 
		pin = random.sample(xrange(10), 4)
		self.download_pin =  "".join([str(x) for x in pin])

	def send_email(self):
		unique_url = settings.SITE_URL+'download/'+self.download_token

		context = {
		'subject': "Your "+self.album.name+" Digital Download",
		'album':self.album,
		'purchase':self,
		'unique_url':unique_url,
		'site_url':settings.SITE_URL[:-1],
		}

		sendPurchaseEmail('', context, self)


	def save(self, *args, **kwargs):
		if not self.pk:
			# New purchase
			self.generate_link()
			self.generate_pin()

			self.send_email()

		if not self.download_token:
			self.generate_link()

		if not self.download_pin:
			self.generate_pin()
		super(Purchase, self).save(*args, **kwargs)

	def get_verbose_name(self):
		return (self.email + ": " + self.album.name).encode('utf-8')

	def __unicode__(self):
		return self.get_verbose_name()

	def __str__(self):
		return self.get_verbose_name()




from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from albums.models import Album
import hashlib, random

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.CharField(max_length=500, null=True, blank=True, verbose_name="website")

    def __unicode__(self):
        return str(self.user)

class Purchase(models.Model):
	user = models.ForeignKey(User)
	album = models.ForeignKey(Album)
	time = models.DateTimeField(auto_now=True)

	download_link = models.URLField(max_length=500, blank=True, null=True)
	download_pin = models.CharField(max_length=10, blank=True, null=True)

	def stripe_charge(self):
		pass

	def generate_link(self):
		# Hash user email and date purchased to create unique link
		user_email = str(self.user.email)
		date_purchased = str(self.time)
		hashed = hashlib.sha256((user_email + date_purchased).encode('utf-8')).hexdigest()
		self.download_link = settings.SITE_URL+settings.DOWNLOAD_URL + hashed

	def generate_pin(self):
		# Generate random 
		pin = random.sample(xrange(10), 4)
		self.download_pin =  "".join([str(x) for x in pin])

	def save(self, *args, **kwargs):
		if not self.pk:
			# New purchase
			self.generate_link()
			self.generate_pin()

		if not self.download_link:
			self.generate_link()

		if not self.download_pin:
			self.generate_pin()
		super(Purchase, self).save(*args, **kwargs)

	def get_verbose_name(self):
		return (self.user.email + ": " + self.album.name).encode('utf-8')

	def __unicode__(self):
		return self.get_verbose_name()

	def __str__(self):
		return self.get_verbose_name()




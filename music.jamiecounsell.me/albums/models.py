from django.db import models
from django.conf import settings
from albums.fields import ExclusiveBooleanField
from albums.validators import photo_validator
import hashlib

class Album(models.Model):
	add_date 	= models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Date created.")
	name 		= models.CharField(max_length=100, null=False, blank=False, help_text="Enter the full album name here.")
	
	is_single	= models.BooleanField(default=False, verbose_name="Single", help_text="Check this box if the album is a single.")
	
	cover_art	= models.ImageField(upload_to="cover_art/", validators=[photo_validator])
	background	= models.ImageField(upload_to="backgrounds/", validators=[photo_validator])
	
	description	= models.TextField(blank=True, null=True)

	featured 	= ExclusiveBooleanField(default=False, verbose_name="Feature this Album.", help_text="Only one album can be featured at a time.")

	price 		= models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Price ($)", help_text="Please enter a price. Dollars and cents can be used (ie. 4.99).")
	
	@property
	def price_incents(self):
		return int(self.price * 100)

	@property
	def price_read(self):
		return '${:,.2f}'.format(self.price)

	def readable_name(self):
		return self.name

	def __unicode__(self):
		return self.readable_name()

	def __str__(self):
		return self.readable_name()

class Track(models.Model):
	name 	= models.CharField(max_length=200, null=False,blank=False, help_text="Track name.")
	album 	= models.ForeignKey(Album)
	price 	= models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2, help_text="Individual price. Leave blank if the track is not to be sold individually.")
	audio_file = models.FileField(upload_to='tracks/')

	@property
	def price_incents(self):
		return int(self.price * 100)

	@property
	def price_read(self):
		return '${:,.2f}'.format(self.price)

	def readable_name(self):
		return self.name

	def __unicode__(self):
		return self.readable_name()

	def __str__(self):
		return self.readable_name()

class TrackToken(models.Model):
	track 	= models.ForeignKey(Track)
	date 	= models.DateTimeField(auto_now=True)
	token 	= models.CharField(max_length=500)

	def save(self, *args, **kwargs):
		if not self.token:
			self.token = hashlib.sha256((self.track.name + str(self.date)).encode('utf-8')).hexdigest()
		super(TrackToken, self).save(*args, **kwargs)

class BonusContent(models.Model):
	name 	= models.CharField(max_length=200, null=False,blank=False, help_text="Track name.")
	album 	= models.ForeignKey(Album)
	bonus_file = models.FileField(upload_to='bonus/')


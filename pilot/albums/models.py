from django.db import models
from django.conf import settings
from albums.fields import ExclusiveBooleanField
from albums.validators import photo_validator
from albums.utilities import slugger, trackSort
from django.db.models.signals import post_save
from colorfield.fields import ColorField
import hashlib, re
import zipfile, StringIO, os

class Album(models.Model):
	add_date 	= models.DateTimeField(auto_now=True, null=False, blank=False, verbose_name="Date created.")
	name 		= models.CharField(max_length=100, null=False, blank=False, help_text="Enter the full album name here.")
	
	is_single	= models.BooleanField(default=False, verbose_name="Single", help_text="Check this box if the album is a single.")
	hidden		= models.BooleanField(default=False, null=False, blank=False, verbose_name="Hide Album", help_text="Yes: Album will be hidden from view. No: Album will be visible through its URL and the homepage.")
	released 	= models.BooleanField(default=True, null=False, blank=False, help_text="Check this box if the album is released for sale.")
	cover_art	= models.ImageField(upload_to="cover_art/", validators=[photo_validator])
	background	= models.ImageField(upload_to="backgrounds/", validators=[photo_validator])
	
	description	= models.TextField(blank=True, null=True)

	featured 	= ExclusiveBooleanField(default=False, verbose_name="Feature this Album.", help_text="Only one album can be featured at a time.")

	price 		= models.DecimalField(max_digits=5, decimal_places=2, default=0, verbose_name="Price ($)", help_text="Please enter a price. Dollars and cents can be used (ie. 4.99).")
	
	slug 		= models.SlugField(max_length=200, unique=True, null=True, blank=True)

	color		= ColorField()#RGBColorField(verbose_name="Theme color")

	zipfile = models.FileField(null=True, blank=True)

	@property
	def price_incents(self):
		return int(self.price * 100)

	@property
	def price_read(self):
		return '${:,.2f}'.format(self.price)

	@property
	def absolute_url(self):
	    return settings.SITE_URL + "album/" + self.slug

	def readable_name(self):
		return self.name + " [single]" if self.is_single else self.name

	@property
	def url_encoded_name(self):
		return re.sub(" ", "%20", self.name)

	def __unicode__(self):
		return self.readable_name()

	def __str__(self):
		return self.readable_name()

	def createZipFile(self):
		print settings.MEDIA_ROOT
		bonus = BonusContent.objects.filter(album=self.pk)
		bonus_files = [open(f.bonus_file.path, 'rb') for f in bonus]

		tracks = trackSort(list(Track.objects.filter(album=self.pk)))
		track_files = [open(f.audio_file.path, 'rb') for f in tracks]

		with zipfile.ZipFile(os.path.join(settings.MEDIA_ROOT, "zip/album_"+str(self.pk)), 'w') as zip:
			for i, f in enumerate(track_files):
				f.seek(0)
				num = tracks[i].track_number
				name = tracks[i].name
				ext = os.path.basename(f.name).split('.')[-1]
				zip.writestr("{0} - {1}.{2}".format(num, name, ext), f.read())
				f.close()
			for i, f in enumerate(bonus_files):
				name = bonus[i].name
				ext = os.path.basename(f.name).split('.')[-1]
				zip.writestr("{0}.{1}".format(name, ext), f.read())
			self.zipfile = os.path.join(settings.MEDIA_ROOT, "zip/album_"+str(self.pk))
			zip.close()

	def save(self, *args, **kwargs):
		self.createZipFile()
		super(Album, self).save(*args, **kwargs)

class Track(models.Model):
	track_number = models.PositiveSmallIntegerField()
	name 	= models.CharField(max_length=200, null=False,blank=False, help_text="Track name.")
	album 	= models.ForeignKey(Album)
	price 	= models.DecimalField(max_digits=5, null=True, blank=True, decimal_places=2, help_text="Individual price. Leave blank if the track is not to be sold individually.")
	audio_file = models.FileField(upload_to='tracks/', null=True, blank=True)

	lyrics	= models.TextField(blank=True, null=True)

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
	date 	= models.FloatField()
	token 	= models.CharField(max_length=500)
	counter = models.IntegerField(default=0, blank=False, null=False)

	def save(self, *args, **kwargs):
		if not self.token:
			self.token = hashlib.sha256((self.track.name + str(self.date)).encode('utf-8')).hexdigest()
		super(TrackToken, self).save(*args, **kwargs)

class BonusContent(models.Model):
	name 	= models.CharField(max_length=200, null=False,blank=False, help_text="Track name.")
	album 	= models.ForeignKey(Album)
	bonus_file = models.FileField(upload_to='bonus/')

post_save.connect(slugger, sender=Album)

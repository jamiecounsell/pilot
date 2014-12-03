from PIL import Image
from django.utils.translation import ugettext as _
from django.core.exceptions import ValidationError
from django.conf import settings

def photo_validator(image):
	try:
		img = Image.open(image)
	except Exception as e:
		print e
	if img:
		photo_type = image.field.attname
		w, h = img.size
		if photo_type == "background":
			max_width , max_height= settings.PX_SIZE_BACKGROUND
			max_size = settings.MB_SIZE_BACKGROUND
		elif photo_type == "cover_art":
			max_width, max_height = settings.PX_SIZE_COVER_ART
			max_size = settings.MB_SIZE_COVER_ART
		else:
			# This should never happen. It means you're using the validator
			# on a field whose settings aren't defined.
			raise ValidationError(_("ValidationError. Contact a developer!"))

		#validate dimensions
		if w > max_width or h > max_height:
			raise ValidationError(
			_('Please use an image that is smaller or equal to '
			'%s x %s pixels.' % (max_width, max_height)))

		#validate content type
		sub = img.format
		if not (sub.lower() in settings.ALLOWED_IMAGE_FORMATS):
			raise ValidationError(_('Please use a JPEG or PNG image.'))

		#validate file size
		if len(image) > (max_size * 1024 * 1024):
			raise ValidationError(_('Image file too large. Maximum size: %dMb' % (max_size)))
	else:
		print "wat"
		raise ValidationError(_("Couldn't read uploaded image"))
	return image
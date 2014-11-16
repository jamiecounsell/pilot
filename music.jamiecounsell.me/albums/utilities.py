from django.utils.text import slugify 


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

def slugger(sender, **kwargs):
	self = kwargs['instance']
	created = kwargs['created']
	if not self.slug:
		_slug = "-".join(unicode(self.name).split())+"-"+unicode(self.pk)
		if len(_slug) > 200:
			_slug = unicode(self.pk)
		try:
			_slug = slugify(_slug)
			sender.objects.filter(pk=self.pk).update(slug=_slug)
		except Exception as e:
			print e
			print "wat"
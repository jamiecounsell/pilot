from django.utils.text import slugify
from django import forms
from django.conf import settings
from django import forms
from django.conf import settings

class FileIterWrapper(object):

    def __init__(self, flo, chunk_size=1024 ** 2):
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
        _slug = "-".join(unicode(self.name).split()) + "-" + unicode(self.pk)
        if len(_slug) > 200:
            _slug = unicode(self.pk)
        try:
            _slug = slugify(_slug)
            sender.objects.filter(pk=self.pk).update(slug=_slug)
        except Exception as e:
            print e
            print "wat"


def trackSort(t_list):
    for i in range(1, len(t_list)):
        tmp = t_list[i]
        k = i
        while k > 0 and int(tmp.track_number) < int(t_list[k - 1].track_number):
            t_list[k] = t_list[k - 1]
            k -= 1
        t_list[k] = tmp

    return t_list

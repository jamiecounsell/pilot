# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0010_bonuscontent_tracktoken'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracktoken',
            name='album',
        ),
        migrations.AddField(
            model_name='tracktoken',
            name='track',
            field=models.ForeignKey(default=None, to='albums.Track'),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0015_track_lyrics'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracktoken',
            name='track_number',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]

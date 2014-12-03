# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0016_tracktoken_track_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracktoken',
            name='track_number',
        ),
        migrations.AddField(
            model_name='track',
            name='track_number',
            field=models.PositiveSmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]

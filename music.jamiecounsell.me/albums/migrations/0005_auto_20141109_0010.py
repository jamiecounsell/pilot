# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_auto_20141108_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='background',
            field=models.ImageField(upload_to=b'/Users/jamiecounsell/Dropbox (Personal)/Developer/music.jamiecounsell.me/music/public/backgrounds/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='cover_art',
            field=models.ImageField(upload_to=b'/Users/jamiecounsell/Dropbox (Personal)/Developer/music.jamiecounsell.me/music/public/cover_art/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='description',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='track',
            name='audio_file',
            field=models.FileField(upload_to=b'/Users/jamiecounsell/Dropbox (Personal)/Developer/music.jamiecounsell.me/music/public/tracks/'),
            preserve_default=True,
        ),
    ]

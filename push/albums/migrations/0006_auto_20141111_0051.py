# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import albums.fields


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0005_auto_20141109_0010'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='featured',
            field=albums.fields.ExclusiveBooleanField(default=False, help_text=b'Only one album can be featured at a time.', verbose_name=b'Feature this Album.'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='background',
            field=models.ImageField(upload_to=b'backgrounds/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='cover_art',
            field=models.ImageField(upload_to=b'cover_art/'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='track',
            name='audio_file',
            field=models.FileField(upload_to=b'tracks/'),
            preserve_default=True,
        ),
    ]

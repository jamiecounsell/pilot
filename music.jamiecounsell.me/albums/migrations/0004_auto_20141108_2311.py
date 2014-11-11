# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0003_auto_20141108_2259'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='audio_file',
            field=models.FileField(default=None, upload_to=b'tracks/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='name',
            field=models.CharField(default=None, help_text=b'Track name.', max_length=200),
            preserve_default=False,
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
    ]

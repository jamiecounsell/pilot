# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import albums.validators


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0006_auto_20141111_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='background',
            field=models.ImageField(upload_to=b'backgrounds/', validators=[albums.validators.photo_validator]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='cover_art',
            field=models.ImageField(upload_to=b'cover_art/', validators=[albums.validators.photo_validator]),
            preserve_default=True,
        ),
    ]

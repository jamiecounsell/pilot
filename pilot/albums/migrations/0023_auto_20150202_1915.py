# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0022_auto_20150201_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='color',
            field=colorfield.fields.ColorField(max_length=10),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='track',
            name='audio_file',
            field=models.FileField(null=True, upload_to=b'tracks/', blank=True),
            preserve_default=True,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import colorful.fields


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0021_album_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='color',
            field=colorful.fields.RGBColorField(),
            preserve_default=True,
        ),
    ]

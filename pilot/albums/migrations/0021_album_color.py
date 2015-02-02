# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import albums.utilities


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0020_auto_20141210_0052'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='color',
            field=albums.utilities.ColorField(default='', max_length=10),
            preserve_default=False,
        ),
    ]

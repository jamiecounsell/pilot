# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0012_album_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracktoken',
            name='date',
            field=models.FloatField(),
            preserve_default=True,
        ),
    ]

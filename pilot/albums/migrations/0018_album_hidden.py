# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0017_auto_20141125_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='hidden',
            field=models.BooleanField(default=False, help_text=b'Yes: Album will be hidden from view. No: Album will be visible through its URL and the homepage.', verbose_name=b'Hide Album'),
            preserve_default=True,
        ),
    ]

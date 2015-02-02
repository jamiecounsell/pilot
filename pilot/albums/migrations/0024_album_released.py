# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0023_auto_20150202_1915'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='released',
            field=models.BooleanField(default=True, help_text=b'Check this box if the album is released for sale.'),
            preserve_default=True,
        ),
    ]

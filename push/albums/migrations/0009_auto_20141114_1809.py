# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0008_album_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='add_date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 14, 18, 9, 20, 803201, tzinfo=utc), verbose_name=b'Date created.', auto_now=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='track',
            name='price',
            field=models.DecimalField(help_text=b'Individual price. Leave blank if the track is not to be sold individually.', null=True, max_digits=5, decimal_places=2, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='price',
            field=models.DecimalField(default=0, help_text=b'Please enter a price. Dollars and cents can be used (ie. 4.99).', verbose_name=b'Price ($)', max_digits=5, decimal_places=2),
            preserve_default=True,
        ),
    ]

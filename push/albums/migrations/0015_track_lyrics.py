# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0014_tracktoken_counter'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='lyrics',
            field=models.TextField(null=True, blank=True),
            preserve_default=True,
        ),
    ]

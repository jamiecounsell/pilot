# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0013_auto_20141116_0221'),
    ]

    operations = [
        migrations.AddField(
            model_name='tracktoken',
            name='counter',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]

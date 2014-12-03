# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20141116_2352'),
    ]

    operations = [
        migrations.RenameField(
            model_name='purchase',
            old_name='download_link',
            new_name='download_token',
        ),
    ]

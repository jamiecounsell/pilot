# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0002_auto_20150103_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='songtrackingrecord',
            name='milestone',
            field=models.ForeignKey(help_text=b'The most recent or final milestone that was hit by the user.', to='tracking.SongTrackingMilestone'),
            preserve_default=True,
        ),
    ]

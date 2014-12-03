# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20141109_0013'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='user',
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
        migrations.RemoveField(
            model_name='purchase',
            name='user',
        ),
        migrations.AddField(
            model_name='purchase',
            name='email',
            field=models.CharField(max_length=100, null=True, verbose_name=b'User Email', blank=True),
            preserve_default=True,
        ),
    ]

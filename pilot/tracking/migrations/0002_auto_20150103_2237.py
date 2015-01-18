# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SongTrackingRecord',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True, auto_now_add=True)),
                ('milestone', models.ForeignKey(to='tracking.SongTrackingMilestone')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='songtrackingmilestone',
            name='mark',
            field=models.DecimalField(help_text=b'Enter a value between 0 and 1. For example, 0.50 for a mark at 50%. ', max_digits=2, decimal_places=2, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(1)]),
            preserve_default=True,
        ),
    ]

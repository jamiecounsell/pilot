# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0002_album_is_single'),
    ]

    operations = [
        migrations.CreateModel(
            name='Track',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('album', models.ForeignKey(to='albums.Album')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='album',
            name='is_single',
            field=models.BooleanField(default=False, help_text=b'Check this box if the album is a single.', verbose_name=b'Single'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='album',
            name='name',
            field=models.CharField(help_text=b'Enter the full album name here.', max_length=100),
            preserve_default=True,
        ),
    ]

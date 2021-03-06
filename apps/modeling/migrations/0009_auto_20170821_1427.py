# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 21:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modeling', '0008_auto_20170821_1322'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='photography_album_1',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='album1', to='modeling.Album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='photography_album_2',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='album2', to='modeling.Album'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='photography_album_3',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='album3', to='modeling.Album'),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='photo',
            name='master_album',
        ),
        migrations.AddField(
            model_name='photo',
            name='master_album',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='modeling.Album'),
            preserve_default=False,
        ),
    ]

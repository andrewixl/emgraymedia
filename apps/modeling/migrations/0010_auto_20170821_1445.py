# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 21:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modeling', '0009_auto_20170821_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='home',
            old_name='photography_album_1',
            new_name='modeling_album_1',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='photography_album_2',
            new_name='modeling_album_2',
        ),
        migrations.RenameField(
            model_name='home',
            old_name='photography_album_3',
            new_name='modeling_album_3',
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 18:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeling', '0002_album_album_cover'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='home',
            name='slide_1',
        ),
        migrations.AddField(
            model_name='home',
            name='slide_1',
            field=models.ImageField(default='media/None/no-img.jpg', upload_to='media/'),
        ),
        migrations.RemoveField(
            model_name='home',
            name='slide_2',
        ),
        migrations.AddField(
            model_name='home',
            name='slide_2',
            field=models.ImageField(default='media/None/no-img.jpg', upload_to='media/'),
        ),
        migrations.RemoveField(
            model_name='home',
            name='slide_3',
        ),
        migrations.AddField(
            model_name='home',
            name='slide_3',
            field=models.ImageField(default='media/None/no-img.jpg', upload_to='media/'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-25 04:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeling', '0026_auto_20170824_2112'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='album_description',
            field=models.CharField(max_length=350, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_location',
            field=models.CharField(max_length=150, verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='album',
            name='album_photographer',
            field=models.CharField(max_length=350, verbose_name='Photographer (Instagram Handle)'),
        ),
        migrations.AlterField(
            model_name='album',
            name='shoot_date',
            field=models.DateField(verbose_name='Shoot Date'),
        ),
    ]

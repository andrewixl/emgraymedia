# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 23:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeling', '0013_auto_20170821_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='package_inclusions',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='package',
            name='package_description',
            field=models.CharField(max_length=500),
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-08-25 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='instagram',
            field=models.CharField(default='andrewixl', max_length=100),
            preserve_default=False,
        ),
    ]
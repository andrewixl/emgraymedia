# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-21 20:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeling', '0007_auto_20170821_1153'),
    ]

    operations = [
        migrations.AddField(
            model_name='home',
            name='profile_description_line_1',
            field=models.CharField(default='fdsafdsaf', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='profile_description_line_2',
            field=models.CharField(default='ffgdssfdas', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='profile_description_line_3',
            field=models.CharField(default='fdaafdsf', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='profile_name',
            field=models.CharField(default='fdsfsdf', max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='home',
            name='profile_picture',
            field=models.ImageField(default='media/None/no-img.jpg', upload_to='media/'),
        ),
        migrations.AddField(
            model_name='home',
            name='profile_title',
            field=models.CharField(default='fdfkasdfkjhasdkjf', max_length=250),
            preserve_default=False,
        ),
    ]

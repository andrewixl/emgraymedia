# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-23 23:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modeling', '0017_auto_20170821_2230'),
    ]

    operations = [
        migrations.CreateModel(
            name='Navbar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_1', models.CharField(max_length=45)),
                ('about_2', models.CharField(max_length=45)),
                ('about_3', models.CharField(max_length=45)),
                ('about_4', models.CharField(max_length=45)),
                ('portfolio_header_1', models.CharField(max_length=45)),
                ('portfolio_1_action_1', models.CharField(max_length=45)),
                ('portfolio_1_action_2', models.CharField(max_length=45)),
                ('portfolio_header_2', models.CharField(max_length=45)),
                ('portfolio_2_action_1', models.CharField(max_length=45)),
                ('portfolio_2_action_2', models.CharField(max_length=45)),
                ('portfolio_header_3', models.CharField(max_length=45)),
                ('portfolio_3_action_1', models.CharField(max_length=45)),
                ('portfolio_3_action_2', models.CharField(max_length=45)),
            ],
        ),
    ]

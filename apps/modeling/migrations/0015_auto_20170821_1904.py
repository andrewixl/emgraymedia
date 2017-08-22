# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-22 02:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modeling', '0014_auto_20170821_1614'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='photography_package_1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package1p', to='modeling.Package'),
        ),
        migrations.AlterField(
            model_name='home',
            name='photography_package_2',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package2p', to='modeling.Package'),
        ),
        migrations.AlterField(
            model_name='home',
            name='photography_package_3',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='package3p', to='modeling.Package'),
        ),
    ]

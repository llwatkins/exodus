# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 22:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_query', '0021_auto_20170924_2212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisrequest',
            name='apk',
            field=models.FileField(upload_to='apks/d1c63d52-ac39-4709-9fe1-22553f7a54d1'),
        ),
        migrations.AlterField(
            model_name='analysisrequest',
            name='storage_path',
            field=models.TextField(default='apks/d1c63d52-ac39-4709-9fe1-22553f7a54d1'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-24 21:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_query', '0002_auto_20170924_2130'),
    ]

    operations = [
        migrations.AlterField(
            model_name='analysisrequest',
            name='apk',
            field=models.FileField(upload_to='apks/e3c24606-9a8b-476b-b0e6-cfcb75fb2af3'),
        ),
        migrations.AlterField(
            model_name='analysisrequest',
            name='storage_path',
            field=models.TextField(default='apks/e3c24606-9a8b-476b-b0e6-cfcb75fb2af3'),
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-19 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20170903_2206'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='pinned',
            field=models.BooleanField(default=False),
        ),
    ]
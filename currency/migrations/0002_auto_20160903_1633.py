# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-03 07:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='opposite_nation',
            field=models.CharField(default=datetime.datetime(2016, 9, 3, 7, 33, 26, 44407, tzinfo=utc), max_length=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='currency',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 9, 3, 7, 33, 44, 418804, tzinfo=utc), verbose_name='published date'),
            preserve_default=False,
        ),
    ]

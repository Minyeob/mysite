# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-08-22 06:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='mod_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 8, 22, 6, 56, 10, 922139, tzinfo=utc), verbose_name='date modified'),
            preserve_default=False,
        ),
    ]
# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-18 12:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0012_auto_20160910_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencycny',
            name='pub_date',
            field=models.DateField(default=datetime.date(2016, 9, 18), verbose_name='published date'),
        ),
        migrations.AlterField(
            model_name='currencyeur',
            name='pub_date',
            field=models.DateField(default=datetime.date(2016, 9, 18), verbose_name='published date'),
        ),
        migrations.AlterField(
            model_name='currencygbp',
            name='pub_date',
            field=models.DateField(default=datetime.date(2016, 9, 18), verbose_name='published date'),
        ),
        migrations.AlterField(
            model_name='currencyjpy',
            name='pub_date',
            field=models.DateField(default=datetime.date(2016, 9, 18), verbose_name='published date'),
        ),
        migrations.AlterField(
            model_name='currencykrw',
            name='pub_date',
            field=models.DateField(default=datetime.date(2016, 9, 18), verbose_name='published date'),
        ),
    ]

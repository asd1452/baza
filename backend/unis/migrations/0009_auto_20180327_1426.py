# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-03-27 12:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('unis', '0008_auto_20180327_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='zaposlenik',
            name='uloga_eng',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='zaposlenik',
            name='kategorija',
            field=models.CharField(choices=[('MA', 'Menadžment'), ('PR', 'Prodaja i računovodstvo'), ('TP', 'Tehnička podrška')], max_length=2),
        ),
    ]

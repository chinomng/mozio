# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('area', django.contrib.gis.db.models.fields.PolygonField(srid=4326)),
                ('price', models.DecimalField(max_digits=8, decimal_places=3)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('lang', models.CharField(max_length=10)),
                ('email_address', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=15)),
                ('currency', models.CharField(max_length=3)),
            ],
        ),
        migrations.AddField(
            model_name='area',
            name='provider',
            field=models.ForeignKey(to='geoapi.Provider'),
        ),
    ]

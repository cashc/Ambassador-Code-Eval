# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-04 02:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.TextField()),
                ('clicks', models.IntegerField()),
            ],
        ),
    ]
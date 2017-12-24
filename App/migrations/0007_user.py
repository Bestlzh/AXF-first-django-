# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-08 05:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_foodtype_goods'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('userName', models.CharField(max_length=20, unique=True)),
                ('userPasswd', models.CharField(max_length=20)),
                ('userPhone', models.CharField(max_length=20)),
                ('userAdderss', models.CharField(max_length=100)),
                ('userImg', models.CharField(max_length=150)),
                ('userRank', models.IntegerField()),
            ],
        ),
    ]

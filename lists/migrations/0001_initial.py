# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-12-13 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('plName', models.CharField(default='', help_text='Your name', max_length=40)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-25 15:41
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gigs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('datetime', models.DateTimeField()),
                ('venue', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gigs.Venue')),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-11-20 18:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('palestras', '0001_initial'),
        ('eventos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='palestra',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='palestras.Palestra'),
        ),
    ]

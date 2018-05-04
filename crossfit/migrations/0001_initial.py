# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-03 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CrossfitCenter',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=None, max_length=10, null=True)),
                ('address', models.TextField(default=None, null=True)),
                ('PhoneNum', models.CharField(default=None, max_length=13, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CrossfitMember',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('password', models.CharField(default='1111', max_length=20)),
                ('name', models.CharField(default=None, max_length=20, null=True)),
                ('PhoneNum', models.CharField(default=None, max_length=13, null=True)),
                ('center_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crossfit.CrossfitCenter')),
            ],
        ),
        migrations.CreateModel(
            name='WorkoutRecord',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('workoutName', models.CharField(default=None, max_length=20, null=True)),
                ('recordTime', models.TimeField(default=None, null=True)),
                ('recordedDate', models.DateTimeField(default=None, null=True)),
                ('MemberId', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='crossfit.CrossfitMember')),
            ],
        ),
    ]
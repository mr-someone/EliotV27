# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-11 10:10
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Device',
            fields=[
                ('device_c_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('balance', models.FloatField(default=0)),
                ('usage', models.FloatField(default=0)),
                ('status', models.IntegerField(default=0)),
                ('last_update', models.DateTimeField(auto_now=True)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DeviceLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('log_time', models.DateTimeField(auto_created=True)),
                ('remaining_balance', models.FloatField(default=0)),
                ('usage', models.FloatField(default=0)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerDash.Device')),
            ],
        ),
        migrations.CreateModel(
            name='Recharge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('gateway_name', models.CharField(max_length=100)),
                ('transaction_id', models.CharField(max_length=100)),
                ('device_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CustomerDash.Device')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('g_id', models.CharField(max_length=100)),
                ('f_id', models.CharField(max_length=100)),
                ('aadhar', models.CharField(default='N/A', max_length=50)),
                ('mob', models.CharField(default='N/A', max_length=15)),
                ('address', models.CharField(default='N/A', max_length=200)),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
